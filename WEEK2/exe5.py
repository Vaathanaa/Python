citydata = [
    ("Phnom Penh",11.5564,104.9282),
    ("Siem Reap",13.3622,103.8597)
]
def displaydata(data_list):
    for city_name, latitude, longitude in data_list:
        print(f"City: {city_name}, Latitude: {latitude}, Longitude: {longitude}")
displaydata(citydata)