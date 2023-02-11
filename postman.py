from pprint import pprint
import requests

payload = {
    'amount':1
}
response = requests.get('http://127.0.0.1:5000/api/to-uzs',params=payload)
pprint(response.json())