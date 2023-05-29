
################ This works ##################################################
# import requests

# api_key = '30d4741c779ba94c470ca1f63045390a'

# user_input = input("Enter city: ")

# weather_data = requests.get(
#     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# if weather_data.json()['cod'] == '404':
#     print("No City Found")
# else:
#     weather = weather_data.json()['weather'][0]['main']
#     temp = round(weather_data.json()['main']['temp'])

#     print(f"The weather in {user_input} is: {weather}")
#     print(f"The temperature in {user_input} is: {temp}ºF")
######################################################################################################

import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
import requests
from tkinter import messagebox
from PIL import ImageTk, Image
import ttkbootstrap

# Function to get weather for a city
def get_weather(city):
    API_key = "30d4741c779ba94c470ca1f63045390a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    
    # Parse the response JSON to get weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    print(weather)
    # Placeholder image
    image_url = "https://image.shutterstock.com/image-photo/adventure-on-mountain-bike-260nw-152465639.jpg"
    
    # Get the icon URL and return all the weather information

    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


# Function to search weather for a city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    # If the city is found, unpack the weather information
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")
    
    # get the weather icon image from the URL and update the icon label
    try:
        image = Image.open(requests.get(icon_url, stream=True).raw) # exception handling
    except Exception as err:
        print(err)
        # placeholder url
        placeholder_url = "https://image.shutterstock.com/image-photo/adventure-on-mountain-bike-260nw-152465639.jpg"
        image = Image.open(requests.get(placeholder_url, stream=True).raw)
    
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update the temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}degC")
    description_label.configure(text=f"Description: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

#Scrollbar
sf = ScrolledFrame(root, autohide=True)
sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# Entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(sf, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button widget -> to search for the weather information
search_button = ttkbootstrap.Button(sf, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Label widget -> to show the city / country name
location_label = tk.Label(sf,font="Helvetica, 25")
location_label.pack()

# Label widget -> to show the weather icon
icon_label = tk.Label(sf)
icon_label.pack()

# Label widget -> to show the temperature
temperature_label = tk.Label(sf, font="Helvetica, 20")
temperature_label.pack()

# Label widget -> to show the weather description
description_label = tk.Label(sf, font="Helvetica, 20")
description_label.pack()

root.mainloop()