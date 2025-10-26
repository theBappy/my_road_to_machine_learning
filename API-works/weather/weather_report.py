import requests
from datetime import datetime
from utils_function import (
    wind_degree_to_direction,
    unix_timestamp_to_localtime,
    convert_temperature
)

def fetch_weather(api_key, location):
    try:
        complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        return api_data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data: ",e)
        return None
    
def write_to_file(weather_data, temperature_unit):
    try:
        with open("weather_info.txt", "w+") as f:
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            if(
                "name" in weather_data
                and "sys" in weather_data
                and "country" in weather_data["sys"]
            ):
                f.write(
                    "-----------------------------------\n"
                )
                f.write(
                    "-----------------------------------\n"
                )
            
            if "main" in weather_data and "temp" in weather_data["main"]:
                f.write(
                    "\tCurrent temperature is: "
                    + convert_temperature(
                        weather_data["main"]["temp"],
                        temperature_unit
                    )
                    + "\n"
                )
            if "weather" in weather_data and "humidity" in weather_data["main"]:
                f.write(
                    "\tCurrent Humidity: {} %\n".format(
                        weather_data["main"]["humidity"]
                    )
                )

            if "wind" in weather_data and "speed" in weather_data["wind"]:
                f.write(
                    "\tCurrent wind speed : {} km/h \n".format(
                        weather_data["wind"]["speed"]
                    )
                )
            
            if "wind" in weather_data and "deg" in weather_data["wind"]["deg"]:
                f.write(
                    "\tCurrent wind direction: "
                    + wind_degree_to_direction(weather_data["wind"]["deg"])
                    +"\n"
                )

            if (
                "sys" in weather_data
                and "sunrise" in weather_data["sys"]
                and "timezone" in weather_data
            ):
                f.write(
                    "\tToday's sunrise time: "
                    + unix_timestamp_to_localtime(
                        weather_data["sys"]["sunrise"],
                        weather_data["timezone"]
                    )
                    +" \n"
                )

            if (
                "sys" in weather_data
                and "sunset" in weather_data["sys"]
                and "timezone" in weather_data
            ):
                f.write(
                    "\tToday's sunset time: "
                    + unix_timestamp_to_localtime(
                        weather_data["sys"]["sunset"], 
                        weather_data["timezone"]
                    )
                    + "\n"
                )
            print("Weather information written to weather_info.txt")

    except IOError as e:
        print("Error writing to file: ", e)

    
def main():
    print("Welcome to the Weather Information App!")
    print("You need an API key to access weather data from OpenWeatherMap.")
    print(
        "You can obtain your API key by signing up at https://home.openweathermap.org/users/sign_up"
    )
    api_key = input("Please enter your open weather app API key: ")
    location = input("Enter the city name: ")

    temperature_unit = input(
        "Enter the temperature unit. 'C' for Celsius and 'F' for Fahrenheit: "
    )
    if not(temperature_unit.upper() == "C" or temperature_unit.upper() == "F"):
        print("Temperature unit must be either be 'C' or 'F'")
        return
    weather_data = fetch_weather(api_key, location)

    if weather_data:
        if weather_data["cod"] == "401":
            print("Invalid API key")
            return
        
        if weather_data["cod"] == "404":
            print("City not found.")
            return

        write_to_file(weather_data, temperature_unit)

        print(
            "Current city :"
            + weather_data["name"]
            + ", "
            + weather_data["sys"]["country"]
        )

        print(
            "Current temperature is: "
            + convert_temperature(weather_data["main"]["temp"], temperature_unit)
        ) 
        print("Current weather data: " + weather_data["weather"][0]["description"])
        print("Current Humidity: " + weather_data["main"]["humidity"], "%")
        print("Current main speed: ", weather_data["wind"]["speed"], "kmph")

        print(
            "Current wind direction: ",
            wind_degree_to_direction(weather_data["wind"]["deg"])
        )
        print(
            "Today's sunrise time: ",
            unix_timestamp_to_localtime(
                weather_data["sys"]["sunrise"],
                weather_data["timezone"]
            )
        )
        print(
            "Today's sunset data: ",
            unix_timestamp_to_localtime(
                weather_data["sys"]["sunset"],
                weather_data["timezone"]
            )
        )
    else:
        print("Failed to fetch weather data. Please check your input and try again.")

if __name__ == "__main__":
    main()


