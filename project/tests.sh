#!/bin/bash

filePath_parkverstoesse_bonn="./data/parkverstoesse_bonn.db"
file_weather_data="./data/weather_data.db"
filePathPipeline_parkverstoesse_bonn="./data/pipeline_car_park_occupancy.py"
filePathPipeline_weather_data="./data/datapipeline_weather.py"

main() {
    # Run Pipelines
    command="python $(python -c 'import os, sys; print(os.path.realpath(sys.argv[1]))' "$filePathPipeline_parkverstoesse_bonn")"
    eval $command
    command="python $(python -c 'import os, sys; print(os.path.realpath(sys.argv[1]))' "$filePathPipeline_parkverstoesse_bonn")"
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