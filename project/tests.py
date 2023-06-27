import os

filePath_parkverstoesse_bonn = "./data/parkverstoesse_bonn.db"
file_weather_data = "./data/weather_data.db"
filePathPipeline_parkverstoesse_bonn = "./data/pipeline_car_park_occupancy.py"
filePathPipeline_weather_data = "./data/datapipeline_weather.py"   

def main():
    # Run Pipelines
    command = "python " + os.path.abspath(filePathPipeline_parkverstoesse_bonn)
    os.system(command)
    command = "python " + os.path.abspath(filePathPipeline_parkverstoesse_bonn)
    os.system(command)
    
    # Test database existence
    try:
        print("Test database existence")

        # Check if the file exists
        assert os.path.exists(filePath_parkverstoesse_bonn), "File filePath_parkverstoesse_bonn does not exist"
        assert os.path.exists(file_weather_data), "File file_weather_data does not exist"
        print("File exists")

        print("Test completed")

    except AssertionError as error:
        print("Test failed")
        print(error)
    
    
if __name__ == "__main__":
    main()