import requests
import csv
import sqlite3

# Define the URL of the data source
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"

# Define the SQLite database and table names
database_name = "airports.sqlite"
table_name = "airports"

# Fetch the data from the URL
response = requests.get(url)
data = response.text

# Parse the CSV data
csv_reader = csv.reader(data.splitlines(), delimiter=';')
rows = list(csv_reader)

# Extract column names from the first row
column_names = [column.strip() for column in rows[0]]

# Remove the first row (column names)
rows = rows[1:]

# Create the SQLite database connection
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Generate the CREATE TABLE statement
create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for column_name in column_names:
    if column_name in ['column_1', 'column_9']:
        create_table_sql += f"{column_name} INTEGER, "
    elif column_name in ['column_7', 'column_8']:
        create_table_sql += f"{column_name} REAL, "
    else:
        create_table_sql += f"{column_name} TEXT, "
create_table_sql = create_table_sql[:-2] + ")"  # Remove the last comma and space

# Create the table in the database
cursor.execute(create_table_sql)

# Generate the INSERT INTO statement and insert data row by row
insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(column_names))})"
cursor.executemany(insert_sql, rows)

# Commit the changes and close the database connection
conn.commit()
conn.close()
