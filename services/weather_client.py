import requests

def get_coordinates(city):
	url = "https://geocoding-api.open-meteo.com/v1/search"
	params = {"name": city, "count": 1}
	response = requests.get(url, params=params)
	data = response.json()

	if not data.get("results"):
		return None, None

	lat = data["results"][0]["latitude"]
	lon = data["results"][0]["longitude"]
	return lat, lon

def get_weather(city, startdate, enddate):
	lat, lon = get_coordinates(city)

	if lat is None:
	    return {"city" : city, "error" : "City not found"}
	url = "https://archive-api.open-meteo.com/v1/archive"
	params = {
		"latitude" : lat,
		"longitude" : lon,
		"start_date" : startdate,
		"end_date" : enddate,
		"daily" : ["temperature_2m_max", "temperature_2m_min",
			   "precipitation_sum"],
		"timezone" : "auto",
		"temperature_unit" : "fahrenheit"
		}
	response = requests.get(url, params=params)
	data = response.json()

	daily = data.get("daily", {})
	temps_max = daily.get("temperature_2m_max", [])
	temps_min = daily.get("temperature_2m_min", [])
	precip = daily.get("precipitation_sum",[])


	avg_max = round(sum(temps_max) / len(temps_max), 1) if temps_max else None	
	avg_min = round(sum(temps_min) / len(temps_min), 1) if temps_min else None
	avg_rain = round(sum(precip) / len(precip), 1) if precip else None

	return {
		"city" : city,
		"start_date" : startdate,
		"end_date" : enddate,
		"avg_high" : avg_max,
		"avg_low" : avg_min,
		"avg_daily_rain_mm" : avg_rain
	}

def get_weather_for_locations(cities, startdate, enddate):
	results = []
	for city in cities:
		weather = get_weather(city, startdate, enddate)
		results.append(weather)
	return results
