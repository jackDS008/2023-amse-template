#!/bin/bash

# Set the absolute paths of the files
filePath_parkverstoesse_bonn="$(pwd)/data/parkverstoesse_bonn.db"
file_weather_data="$(pwd)/data/weather_data.db"
filePathPipeline_parkverstoesse_bonn="$(pwd)/data/pipeline_car_park_occupancy.py"
filePathPipeline_weather_data="$(pwd)/data/datapipeline_weather.py"

main() {
    # Run Pipelines
    command="python '$filePathPipeline_parkverstoesse_bonn'"
    eval $command
    command="python '$filePathPipeline_parkverstoesse_bonn'"
    eval $command

    # Test database existence
    echo "Test database existence"
    # Check if the file exists
    if [[ -e $filePath_parkverstoesse_bonn && -e $file_weather_data ]]; then
        echo "File exists"
        echo "Test completed"
    else
        echo "Test failed"
        if [[ ! -e $filePath_parkverstoesse_bonn ]]; then
            echo "File $filePath_parkverstoesse_bonn does not exist"
        fi
        if [[ ! -e $file_weather_data ]]; then
            echo "File $file_weather_data does not exist"
        fi
    fi
}

# Call the main function
main

# All tests passed
echo "All tests passed"
exit 0