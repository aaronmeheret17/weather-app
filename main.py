from fetch_weather import fetch_weather_data
from validate_location import validate_location
from redis_cache import cache_weather_data, retrieve_weather_data
import redis

def display_weather_forecast(forecast_data):
    periods = forecast_data['properties']['periods']

    print("\n7-day Weather Forecast:")
    print("="*30)

    for period in periods[:7]:
        day = period['name']
        start_time = period['startTime']
        temperature = period['temperature']
        temp_unit = period['temperatureUnit']
        short_forecast = period['shortForecast']
        precipitation = period.get('probabilityOfPrecipitation', {}).get('value')
        precipitation = f"{precipitation}%" if precipitation is not None else "0%"

        print(f"{day} ({start_time}):")
        print(f"  Temperature: {temperature}°{temp_unit}")
        print(f"  Forecast: {short_forecast}")
        print(f"  Chance of Precipitation: {precipitation}")
        print("-" * 30)

def main():
    while True:
        location = input("Enter your City, ST or ZIP Code: (or type 'exit' to quit): ")

        if location.lower() == 'exit':
            print("Exiting the program.")
            return

        try:
            latitude, longitude = validate_location(location)
            print(f"Found valid U.S. location '{location}'. Latitude: {latitude}, Longitude: {longitude}")
            break
        except ValueError as ve:
            print(f"{ve}")
    
    # Connect to Redis
    try:
        redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    # Fetch weather data
        weather_data = fetch_weather_data(latitude, longitude)

    # Store weather data in Redis
        cache_weather_data(redis_client, "weather_data", weather_data)

    # Retrieve and display weather data from Redis
        retrieved_data = retrieve_weather_data(redis_client, "weather_data")
        display_weather_forecast(retrieved_data)
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
