import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Integer, Text

# Read the CSV file
data = pd.read_csv("https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv", sep=";", engine="python", skiprows=7, skipfooter=4, header=None, encoding="iso-8859-1", usecols = [0,1,2,12,22,32,42,52,62,72])

# Define custom column names
selected_columns = {
    0: 'date',
    1: 'CIN',
    2: 'name',
    12: 'petrol',
    22: 'diesel',
    32: 'gas',
    42: 'electro',
    52: 'hybrid',
    62: 'plugInHybrid',
    72: 'others'
}

# Rename columns
data.rename(columns=selected_columns, inplace=True)

# Convert CIN to 5 digits with leading zeros
data["CIN"] = data["CIN"].astype(int).astype(str).apply(lambda x: x.zfill(5))

# Drop NA
data = data.dropna()

# Set sqlalchemy column types
dtypes = {
    "date": Text(),
    "CIN": Text(),
    "name": Text(),
    "petrol": Integer(),
    "diesel": Integer(),
    "gas": Integer(),
    "electro": Integer(),
    "hybrid": Integer(),
    "plugInHybrid": Integer(),
    "others": Integer()
}

# Write the data to the database
data.to_sql("cars", create_engine("sqlite:///cars.sqlite"), if_exists="replace", index=False, dtype=dtypes)
