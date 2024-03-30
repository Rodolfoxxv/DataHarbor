import requests

url = 'https://www.google.com'
try:
    resp = requests.get(url, timeout=10)
    print(resp.status_code)
except requests.exceptions.Timeout:
    print("A solicitação excedeu o tempo limite")
