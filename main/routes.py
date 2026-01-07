from flask import render_template, request
from clima import get_weather
from . import main

@main.route("/")
def home():
    return render_template('index.html')

@main.route("/weather", methods=['POST'])
def weather():
    city = request.form["city"]
    weather_data = get_weather(city)

    if weather_data:
        return render_template('weather.html', weather=weather_data, city=city)
    else:
        return render_template('index.html', error="Ciudad no encontrada")
