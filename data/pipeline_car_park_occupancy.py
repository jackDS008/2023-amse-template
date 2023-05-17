import pandas as pd
import sqlite3
import requests
import io

# Define the URL of the data source
url = 'https://opendata.bonn.de/sites/default/files/ParkverstoesseBonn2020_0.csv'

# Define the local database file path
database_file = 'data/parkverstoesse_bonn.db'

# Define the table name
table_name = 'parking_violations'

# Pull the data from the URL
response = requests.get(url)
data = response.content.decode('utf-8')

# Create a DataFrame from the CSV data
df = pd.read_csv(io.StringIO(data), sep=';')

# Perform data manipulation (if required)
# Example: Convert column names to lowercase
df.columns = df.columns.str.lower()

# Connect to the SQLite database
conn = sqlite3.connect(database_file)

# Store the DataFrame in the database
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
