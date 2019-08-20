import pyowm
city=input("What city you are interested:")
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')    # You MUST provide a valid API key

# Search for current weather in the city

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
wind_at_place = w.get_wind()
print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius"+" wind is"+str(wind_at_place))
print("In this city "+ w.get_detailed_status())
