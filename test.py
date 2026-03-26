import requests

url = "http://localhost:8000/transcribe"
files = {"file": open("Prueba.m4a", "rb")}
response = requests.post(url, files=files)
print(response.json())