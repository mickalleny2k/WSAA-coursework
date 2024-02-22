import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"

#print(response.json())
def getcurrenttemp():
    response = requests.get(url)
    data = response.json()
    #with open ("weatherdump.json", "w") as fp:
    #    json.dump(data, fp)
    tempObject = data["current"]["temperature_2m"]
    return tempObject

if __name__ == "__main__":
    print(getcurrenttemp())