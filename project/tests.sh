#!/bin/bash

# Test 1: System-level test - Check if output file exists
# if [ -f ../temperature_vs_parking_violations.png ]; then
#     echo "System-level test: Output file exists - PASSED"
# else
#     echo "System-level test: Output file does not exist - FAILED"
#     exit 1
# fi

# Test 2: Data pipeline parkverstoesse_bonn test - Execute data pipeline
python pipeline_car_park_occupancy.py

# Check if the database file exists
if [ -f data/parkverstoesse_bonn.db ]; then
    echo "Data pipeline parkverstoesse_bonn test: Database file created - PASSED"
else
    echo "Data pipeline parkverstoesse_bonn test: Database file not created - FAILED"
    exit 1
fi

# Test 3: Data pipeline weather test - Execute data pipeline
python pipeline_car_park_occupancy.py

# Check if the database file exists
if [ -f data/weather_data.db ]; then
    echo "Data pipeline weather test: Database file created - PASSED"
else
    echo "Data pipeline weather test: Database file not created - FAILED"
    exit 1
fi

# All tests passed
echo "All tests passed"
exit 0
