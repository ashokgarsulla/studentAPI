import requests
import json

URL = "http://127.0.0.1:8000/api/data/create/"

data = {
'name': 'raji',
'roll':12
}
print('python Data',data)
json_data = json.dumps(data)
print('JSON data',json_data)
r = requests.post(url = URL, data = json_data)
print(r)
data = r.json()
print(data)


