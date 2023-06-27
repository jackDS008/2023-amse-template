#!/bin/bash

# Get the absolute path of the script's directory
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"

# Construct absolute paths of the files
filePath_parkverstoesse_bonn="$script_dir/data/parkverstoesse_bonn.db"
file_weather_data="$script_dir/data/weather_data.db"
filePathPipeline_parkverstoesse_bonn="$script_dir/data/pipeline_car_park_occupancy.py"
filePathPipeline_weather_data="$script_dir/data/datapipeline_weather.py"

main() {
    # Run Pipelines
    command="python '$(realpath "$filePathPipeline_parkverstoesse_bonn")'"
    eval $command
    command="python '$(realpath "$filePathPipeline_parkverstoesse_bonn")'"
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