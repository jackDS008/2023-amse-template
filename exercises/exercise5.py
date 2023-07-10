import urllib.request
import zipfile
import pandas as pd
from sqlalchemy import Integer, Text, Float

# Data processing
urllib.request.urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip", "GTFS.zip")
with zipfile.ZipFile("GTFS.zip", 'r') as zip_ref:
    zip_ref.extractall("stops/")
    
columns = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
df = pd.read_csv("stops/stops.txt", delimiter=',', usecols=columns, encoding='utf-8')

df["stop_id"] = df["stop_id"].astype(int)
df["stop_name"] = df["stop_name"].astype(str)
df["stop_lat"] = df["stop_lat"].astype(float)
df["stop_lon"] = df["stop_lon"].astype(float)
df["zone_id"] = df["zone_id"].astype(int)

df = df[df["zone_id"] == 2001]
df = df[(df["stop_lat"] >= -90)]
df = df[(df["stop_lat"] <= 90)]
df = df[(df["stop_lon"] >= -90)]
df = df[(df["stop_lon"] <= 90)]

types = {
    "stop_id" : Integer,
    "stop_name" : Text,
    "stop_lat" : Float,
    "stop_lon" : Float,
    "zone_id" : Integer
    }

df.to_sql("stops", "sqlite:///gtfs.sqlite", if_exists='replace', dtype=types, index=False)