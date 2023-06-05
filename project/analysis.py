import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Import weather
database_path = os.path.join(os.getcwd(), 'data', 'weather_data.db')
conn = sqlite3.connect(database_path)
cursor = conn.cursor()
cursor.execute("SELECT * FROM weather")
rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]
df_weather = pd.DataFrame(rows, columns=column_names)
cursor.close()
conn.close()

# Import parking violations
database_path = os.path.join(os.getcwd(), 'data', 'parkverstoesse_bonn.db')
conn = sqlite3.connect(database_path)
cursor = conn.cursor()
cursor.execute("SELECT * FROM parking_violations")
rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]
df_parking = pd.DataFrame(rows, columns=column_names)
cursor.close()
conn.close()

# Merge data frames
df_parking['hour'] = df_parking['tatzeit'] // 100 # Calculate hour from tatzeit
df_weather['date'] = pd.to_datetime(df_weather['date']).dt.strftime('%d.%m.%Y')
df = pd.merge(df_weather, df_parking, left_on=['date', 'hour'], right_on=['tattag', 'hour'])


### Data analysis ###

# Visualize the distribution of parking violations by time of day
plt.figure(figsize=(10, 5))
plt.hist(df['hour'], bins=24, edgecolor='black')
plt.xlabel('Hour of Day')
plt.ylabel('Frequency')
plt.title('Distribution of Parking Violations by Time of Day')
plt.show()

# Visualize the relationship between air temperature and parking violations (trend)
df['date'] = pd.to_datetime(df['date'])
num_days = (df['date'].max() - df['date'].min()).days + 1
violations_by_temperature = df.groupby(['temperature', 'date']).size().reset_index(name='parking_violations')
average_violations = violations_by_temperature.groupby('temperature')['parking_violations'].mean() / num_days
plt.figure(figsize=(10, 5))
plt.scatter(average_violations.index, average_violations, alpha=0.5)
plt.xlabel('Temperature')
plt.ylabel('Average Parking Violations per Day')
plt.title('Relationship between Air Temperature and Parking Violations\nRelative to the Number of Days')
linear_coefficients = np.polyfit(average_violations.index, average_violations, 1)
linear_trendline = np.poly1d(linear_coefficients)
plt.plot(average_violations.index, linear_trendline(average_violations.index), color='red', label='Linear Trendline')
poly5_coefficients = np.polyfit(average_violations.index, average_violations, 5)
poly5_trendline = np.poly1d(poly5_coefficients)
plt.plot(average_violations.index, poly5_trendline(average_violations.index), color='blue', label='Polynomial (Degree 5) Trendline')
plt.show()

# Calculate correlation coefficients
correlation_matrix = df[['hour', 'temperature']].corr()
print(correlation_matrix)

# Linear regression
X = df[['hour', 'temperature']]
y = range(len(df))
regression_model = LinearRegression()
regression_model.fit(X, y)
print('Intercept:', regression_model.intercept_)
print('Coefficients:', regression_model.coef_)