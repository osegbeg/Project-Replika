import csv

with open("./weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    new_data = []
    for row in data:
        new_data.append(row)
    for temp in new_data[1:]:
        temperature.append(int(temp[1]))
    print(temperature)
