import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"
response = requests.get(url)
#print(response.json())
data = response.json()
#with open ("weatherdump.json", "w") as fp:
#    json.dump(data, fp)

tempObject = data["current"]["temperature_2m"]

print(tempObject)