import requests
import json
import os

def validate_location(location):
    api_key = os.getenv('OPENCAGE_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Make sure the OPENCAGE_API_KEY environment variable is set.")
    url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={api_key}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    for result in data['results']:
        components = result['components']
        country_code = components.get('country_code')
        city = components.get('city')
        state = components.get('state')
        postcode = components.get('postcode')

        # Check for a valid U.S. location and specific components based on input type
        if country_code == 'us':
            if ',' in location:  # Likely a city, state input
                if city and state:
                    coordinates = result['geometry']
                    latitude = coordinates.get('lat')
                    longitude = coordinates.get('lng')
                    return latitude, longitude
            elif location.isdigit() and len(location) == 5:  # Likely a ZIP code
                if postcode and postcode == location:
                    coordinates = result['geometry']
                    latitude = coordinates.get('lat')
                    longitude = coordinates.get('lng')
                    return latitude, longitude

    raise ValueError(f"Could not find a valid U.S. location for '{location}'.")
