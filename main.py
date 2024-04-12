from requests import get


URL = r"https://api.open-elevation.com/api/v1/lookup?locations=41.161758,-8.583933"



params = {
    'locations':
        {
            'latitude': 50.04002401852127,
            'longitude': 22.032856140757406
        }
}

data = get(url=URL, params=params)

print(data.json())
