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
   git clone https://github.com/aaronmeheret17/weather-app
   cd weather-app

2. **Setting up the API Key**:
This project requires an API Key from OpenCageData. 
Follow these steps to obtain your API key.
Visit the OpenCageData website.
Sign up for an account (or log in if you already have one).
Navigate to the API section and generate a new API key.
You should store this key in an environment variable called 'OPENCAGE_API_KEY' to keep it secure.
    On Windows (PowerShell)
        Open your terminal.
        Set the environment variable with: $env:OPENCAGE_API_KEY="your_api_key_here"

    On Windows (Command Prompt)
        Open your terminal.
        Set the environment variable with:
        set OPENCAGE_API_KEY=your_api_key_here

    On macOS/Linux (Bash)
        Open your terminal.
        Set the environment variable with:
        export OPENCAGE_API_KEY="your_api_key_here"


2. Set up a virtual environment:
    python3 -m venv venv
    source venv/bin/activate
    
3. Install dependencies and run
    pip install -r requirements.txt
    python main.py

4. Testing
    python -m unittest test_weather.py



   





