def weather_condition(weather):
    if weather == "sunny":
        return "Wear a hat and carry water"
    elif weather == "rainy":
        return "Take an umbrella"
    elif weather == "snowy":
        return "Wear a warm jacket"
    else:
        return "Check the forecast again"

print(weather_condition("sunny"))
print(weather_condition("rainy"))
print(weather_condition("windy"))
