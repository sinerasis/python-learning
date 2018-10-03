# depends on reqeusts library, installed via pip
import requests

response = requests.get(url = "http://samplebeer.com")

print(response.text)