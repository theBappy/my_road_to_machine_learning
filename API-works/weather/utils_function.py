from datetime import datetime, timedelta

def wind_degree_to_direction(str_wind_degree):
    try:
        wind_degree = int(str_wind_degree)
    except ValueError:
        return "API Wind degree data format error!"

    directions = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
    ]

    index = int((wind_degree + 11.25) // 22.5) % 16
    return directions[index]


def unix_timestamp_to_localtime(str_unix_timestamp, str_timezone_offset_seconds):
    try:
        unix_timestamp = int(str_unix_timestamp)
    except ValueError:
        return "API sunset/sunrise data format error!"
    
    try:
        timezone_offset_seconds = int(str_timezone_offset_seconds)
    except ValueError:
        return "API timezone data format error!"
    
    utc_time = datetime.utcfromtimestamp(unix_timestamp)

    local_time = utc_time + timedelta(seconds=timezone_offset_seconds)

    return local_time.strftime("%Y-%m-%d %H:%M:%S")

def convert_temperature(str_temperature_kelvin, temperature_unit):
    try:
        temperature_k = float(str_temperature_kelvin)
    except ValueError:
        return "API temperature data format error!"
    
    unit = str(temperature_unit).upper()
    if not (unit == "C" or unit == "F"):
        return "Temperature unit must either be 'C' or be 'F'!"
    
    if unit == "C":
        temperature_c = temperature_k - 273.15
        return f"{temperature_c:.2f} °C"
    
    if unit == "F":
        temperature_f = temperature_k * 9/5 - 459.67
        return f"{temperature_f:.2f} °F"


