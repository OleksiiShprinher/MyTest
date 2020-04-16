
import pyowm

owm = pyowm.OWM('670a355f137b53cd44c861a633ecfaa2')  # You MUST provide a valid API key

place_to_check = str(input("Where should I check the weather?: "))

observation = owm.weather_at_place(place_to_check)
w = observation.get_weather()

print('In ' + place_to_check + ' now is ' + w.get_detailed_status())
print('The temperature there is ' + str(w.get_temperature('celsius')['temp']))
