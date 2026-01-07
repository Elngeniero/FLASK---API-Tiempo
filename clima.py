import requests
import os

def get_weather(city):
    api_key = os.environ.get('API_KEY')
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric&lang=es"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        pais = data['sys']['country']
        weather_desc = data['weather'][0]['description']

        return {
            "temperature": main['temp'],
            "humidity": main['humidity'],
            "pressure": main['pressure'],
            "wind_speed": wind['speed'],
            "description": weather_desc,
            "country": pais
        }

    else:
        return {"error": "Ciudad no encontrada"}

# tiempo = get_weather("Santiago")
# print(tiempo)
