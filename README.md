# Weather Forecast Application

## Overview
This application retrieves weather forecasts for a given location using the National Weather Service API and stores the data in a Redis cache. The program validates the user's location, fetches the weather data, and displays a 7-day forecast.

## Prerequisites
- Python 3.8+
- Redis (can be run locally via Docker)
- Docker (optional, for running Redis)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aaronmeheret17/weather-app.git
   cd weather-app

2. Set up a virtual environment:
    python3 -m venv venv
    source venv/bin/activate
    
3. Install dependencies and run
    pip install -r requirements.txt
    python main.py

4. Testing
    python -m unittest test_weather.py



   





