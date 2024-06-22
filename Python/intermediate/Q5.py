def analyze_weather_data(t):
    a = sum(t) / len(t)
    h = max(t)
    l = min(t)
    return a, h, l

temperature_readings = [25, 28, 21, 24, 27]
average_temp, highest_temp, lowest_temp = analyze_weather_data(temperature_readings)
print(f"Average Temperature: {average_temp}")
print(f"Highest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")