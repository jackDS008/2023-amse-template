import pandas as pd
import sqlite3
import urllib.request
import gzip
import io

# Define the URL of the data file
url = "https://bulk.meteostat.net/v2/hourly/10517.csv.gz"

# Define the SQLite database filename
db_filename = "data/weather_data.db"

# Function to download and extract the gzip file
def download_data(url):
    response = urllib.request.urlopen(url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)
    return decompressed_file

# Function to create and populate the SQLite database
def create_database(data):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Create the weather table
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    date TEXT,
                    hour INTEGER,
                    temperature REAL,
                    dew_point REAL,
                    humidity INTEGER,
                    precipitation REAL,
                    snow_depth INTEGER,
                    wind_direction INTEGER,
                    wind_speed REAL,
                    wind_gust REAL,
                    pressure REAL,
                    sunshine INTEGER,
                    weather_condition INTEGER
                )''')

    # Insert data into the weather table
    c.executemany('INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Download and extract the data file
data_file = download_data(url)

# Read the data into a pandas DataFrame
df = pd.read_csv(data_file, delimiter=',', names=['date', 'hour', 'temperature', 'dew_point', 'humidity', 'precipitation', 'snow_depth', 'wind_direction', 'wind_speed', 'wind_gust', 'pressure', 'sunshine', 'weather_condition'], header=0)

# Convert the DataFrame to a list of tuples for SQLite insertion
data = [tuple(x) for x in df.to_numpy()]

# Create the SQLite database and populate it with the data
create_database(data)

print("Data has been successfully stored in the SQLite database.")