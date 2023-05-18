import pandas as pd
from sqlalchemy import create_engine, Integer, Text, CHAR, Float

# Read the CSV file into a pandas DataFrame
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
df = pd.read_csv(url, sep=";")

# Define the SQLite database connection
engine = create_engine("sqlite:///airports.sqlite")

# Convert columns to appropriate SQLite types
column_types = {
    "column_1": Integer(),
    "column_2": Text(),
    "column_3": Text(),
    "column_4": Text(),
    "column_5": Text(),
    "column_6": Text(),
    "column_7": Float(),
    "column_8": Float(),
    "column_9": Integer(),
    "column_10": Float(),
    "column_11": CHAR(),
    "column_12": Text(),
    "geo_punkt": Text()
}

# Write the DataFrame to the SQLite database table
df.to_sql("airports", engine, if_exists="replace", index=False, dtype=column_types)
