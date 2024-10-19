# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

## Objective

This project is designed to develop a real-time data processing system that monitors weather conditions across multiple cities in India and provides summarized insights using rollups and aggregates. The system utilizes weather data from the OpenWeatherMap API and stores daily summaries in a SQLite database for further analysis. The application includes features such as temperature alerts and weather condition summaries.

## Features

1. **Real-time weather data retrieval**: Continuously fetches weather data every 5 minutes for six Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) using the OpenWeatherMap API.
2. **Weather summaries**: Provides daily summaries including:
   - Average temperature
   - Maximum temperature
   - Minimum temperature
   - Dominant weather condition
3. **Temperature alerts**: Triggers alerts when temperatures exceed a user-configurable threshold.
4. **Data storage**: Daily weather summaries are stored in an SQLite database (`weather_data.db`) for persistent storage and further analysis.
5. **Visualization**: Displays historical weather data trends using Matplotlib.
6. **Database querying**: Includes a script (`database.py`) for querying and viewing the stored weather summaries.

## Project Structure

- `main.py`: The main application that retrieves, processes, and stores weather data. It also triggers alerts and generates visualizations.
- `requirements.txt`: Lists the dependencies required to run the project.
- `weather_data.db`: The SQLite database where daily weather summaries are stored.
- `database.py`: A script used to query the database and view weather summaries.
- `README.md`: Documentation for the project.

## Setup Instructions

### Prerequisites

1. Python 3.x
2. A valid API key from [OpenWeatherMap](https://openweathermap.org/) to fetch weather data.

### Dependencies

Before running the project, install the required dependencies listed in the `requirements.txt` file. Run the following command to install them:

```bash
pip install -r requirements.txt

Dependencies include:

requests: To make API calls to the OpenWeatherMap API.
matplotlib: For visualizing the weather summaries.
numpy: For performing calculations on the weather data.
sqlite3: (Built-in with Python) For storing weather data in a local database.

### API Key Setup
Replace the placeholder API key in main.py with your actual OpenWeatherMap API key:

```python
API_KEY = 'your_openweathermap_api_key_here'

### Running the Application
To run the real-time weather monitoring application:

```python
python main.py

This will:

Fetch weather data every 5 minutes.
Store daily summaries in the SQLite database (weather_data.db).
Display the summaries and alerts in the console.
Plot weather trends for each day using Matplotlib.

### Querying the Weather Data
To view the stored weather summaries, run the database.py script:
```python
python database.py

This will fetch and display all records from the weather_summary table in the SQLite database.

### Design Choices
API Integration: The OpenWeatherMap API is used for real-time weather data retrieval. The API provides various parameters like current temperature, perceived temperature, and weather conditions.
Persistent Storage: SQLite is used as a lightweight, file-based database to store daily weather summaries, making it easy to analyze and query historical data.
Visualization: Matplotlib is used to generate plots for daily weather trends, providing insights into average, maximum, and minimum temperatures.
Alerts: The system includes temperature alerts, which are configurable. If the temperature exceeds a user-defined threshold, an alert is generated and displayed in the console.

### Future Enhancements
Support for additional weather parameters: Extend the system to include parameters like humidity and wind speed in rollups and aggregates.
Weather forecasts: Add functionality to retrieve and summarize forecast data from the OpenWeatherMap API.
Email Alerts: Implement email notifications for temperature thresholds or specific weather conditions.

### Testing
The project includes various test cases to ensure the system works as expected:

System setup: Verify that the system starts and connects to the OpenWeatherMap API using a valid API key.
Data retrieval: Simulate API calls at configurable intervals and ensure the system correctly parses weather data for the specified locations.
Temperature conversion: Test the conversion of temperature values from Kelvin to Celsius.
Daily weather summary: Simulate weather updates for several days and verify that summaries (average, maximum, minimum temperatures, dominant condition) are calculated correctly.
Alerting thresholds: Define user-configurable thresholds and simulate weather data that breaches those thresholds to ensure alerts are triggered correctly.

### License
This project is licensed under the MIT License.