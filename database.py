import sqlite3

def read_weather_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # Execute the query to fetch all data from the weather_summary table
    cursor.execute("SELECT * FROM weather_summary")

    # Fetch and display all rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    read_weather_data()
