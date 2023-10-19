import python_weather

import asyncio
import os

ciudad = "Spain-Malaga"

async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get(ciudad)
    
    Fahrenheit = weather.current.temperature
    celsius = (weather.current.temperature - 32)*5/9

    # returns the current day's forecast temperature (int)
    print("Hace una tempertatura de:", Fahrenheit, "Grados Farenheits en Málaga")  
    print("Hace una tempertatura de:", celsius, "Grados Farenheits en Málaga")  
  


if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather())