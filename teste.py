import requests
import json
data = {
    'lat': -23.4984442,
    'lon': -47.4463677
}

a = requests.post('http://127.0.0.1:5000/',json = data)
data = json.loads(a.text)
print(data)