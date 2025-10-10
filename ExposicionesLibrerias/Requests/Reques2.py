import requests
respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)
print(respuesta.text)