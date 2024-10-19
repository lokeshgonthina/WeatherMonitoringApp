import requests
import time
from datetime import datetime, timezone
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import sqlite3

API_KEY = 'your_openweathermap_api_key_here'  # Replace with your OpenWeatherMap API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
INTERVAL = 300  # Interval in seconds (5 minutes)
TEMP_THRESHOLD = 35  # User-configurable threshold
temperature_data = defaultdict(list)
alerts = []

# Database setup
DB_NAME = "weather_data.db"

def init_db():
    # Create a database connection and a table for storing weather summaries
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_summary (
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_daily_summary_to_db(daily_summary):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    for date, summary in daily_summary.items():
        cursor.execute('''
            INSERT INTO weather_summary (date, avg_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    
    conn.commit()
    conn.close()

def fetch_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data for {city}, status code: {response.status_code}")
        return None

def process_weather_data(data):
    main = data['main']
    weather = data['weather'][0]['main']
    dt = datetime.fromtimestamp(data['dt'], timezone.utc).strftime('%Y-%m-%d')  # Updated line

    temp = main['temp']
    feels_like = main['feels_like']

    # Store daily weather data
    temperature_data[dt].append({
        'temp': temp,
        'feels_like': feels_like,
        'condition': weather
    })

    # Check for temperature alerts
    check_alerts(temp)

def check_alerts(temp):
    if temp > TEMP_THRESHOLD:
        alerts.append(f"Alert! Temperature exceeded {TEMP_THRESHOLD}°C: {temp}°C")

def calculate_daily_summary():
    daily_summary = {}
    for date, records in temperature_data.items():
        avg_temp = np.mean([record['temp'] for record in records])
        max_temp = np.max([record['temp'] for record in records])
        min_temp = np.min([record['temp'] for record in records])
        conditions = [record['condition'] for record in records]
        dominant_condition = max(set(conditions), key=conditions.count)

        daily_summary[date] = {
            'average_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }
    return daily_summary

def plot_weather_summary(daily_summary):
    dates = list(daily_summary.keys())
    avg_temps = [summary['average_temp'] for summary in daily_summary.values()]
    max_temps = [summary['max_temp'] for summary in daily_summary.values()]
    min_temps = [summary['min_temp'] for summary in daily_summary.values()]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Average Temperature', marker='o')
    plt.plot(dates, max_temps, label='Max Temperature', marker='o')
    plt.plot(dates, min_temps, label='Min Temperature', marker='o')
    plt.title('Daily Weather Summary')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    print("Weather App started!")
    init_db()  # Initialize the database
    while True:
        for city in CITIES:
            print(f"Fetching weather data for {city}...")
            data = fetch_weather_data(city)
            if data:
                process_weather_data(data)
        
        daily_summary = calculate_daily_summary()
        print("Daily Summary:", daily_summary)
        save_daily_summary_to_db(daily_summary)  # Save the summary to the database
        plot_weather_summary(daily_summary)

        if alerts:
            print("Alerts:", alerts)
            alerts.clear()  # Clear alerts after processing
        
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
