import requests
import json

URL = "http://127.0.0.1:8000/api/data/update/"
def update(id = None):
     data = {
         'id': 10,
        'name': 'RaSHHHO'  
        } 
        # This is Partial Update Because we are not Passing Roll
    
     json_data = json.dumps(data)
     r = requests.put(url = URL , data = json_data)
     data =r.json()
     print(data) 
 
update()
