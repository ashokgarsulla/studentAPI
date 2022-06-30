import requests
import json

URL = "http://127.0.0.1:8000/api/data/delete/"
def delete():
     data = {
         'id': 15} 
        # for delete id is giving
     json_data = json.dumps(data)
     r = requests.delete(url = URL , data = json_data)
     data =r.json()
     print(data) 
 
delete()
