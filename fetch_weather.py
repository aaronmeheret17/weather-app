import requests

def fetch_weather_data(latitude, longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    forecast_url = data['properties']['forecast']
    
    forecast_response = requests.get(forecast_url)
    forecast_response.raise_for_status()
    forecast_data = forecast_response.json()
    
    return forecast_data

