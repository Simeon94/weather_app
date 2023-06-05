# import requests

# API_KEY = "30d4741c779ba94c470ca1f63045390a"  # Replace with your OpenWeatherMap API key
# city = "New York"  # Replace with the desired city
# start_timestamp = 1640908800  # Replace with the desired start timestamp (in UTC)
# end_timestamp = 1640995200  # Replace with the desired end timestamp (in UTC)

# url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=40.7128&lon=-74.0060&start={start_timestamp}&end={end_timestamp}&appid={API_KEY}"

# response = requests.get(url)

# if response.status_code == 200:
#     weather_data = response.json()
#     print(weather_data)
#     # Process the weather data as needed
#     # Access the historical hourly weather information from the "hourly" key in the weather_data dictionary
#     hourly_data = weather_data["hourly"]
    
#     # Iterate over each hourly data point and extract specific information
#     for hourly in hourly_data:
#         timestamp = hourly["dt"]  # Unix timestamp of the data point
#         temperature = hourly["temp"]  # Temperature in Kelvin
#         humidity = hourly["humidity"]  # Humidity percentage
        
#         # Continue processing or store the extracted information based on your requirements
# else:
#     print("Error occurred:", response.status_code)

