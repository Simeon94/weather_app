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

# def reverse_number(a):
#     #a =200
#     new_list =[]
#     for i in range(1,a+1):
#         #print(i)
#         new_list.append(str(i))
#         #print(new_list)
#         for j in range(len(new_list)):
#             soln= "".join(new_list[-1::-1])
#     return soln
# print(reverse_number(5))

def reverse_number_pattern(start_number):
    for i in range(start_number, 0, -1):  # Iterate from start_number to 1
        for j in range(i, 0, -1):  # Iterate from i to 1
            print(j, end='')
        print()  # Print a new line after each row

# Test the function
start_number = int(input("Enter the starting number: "))
reverse_number_pattern(start_number)

print(reverse_number_pattern(5))