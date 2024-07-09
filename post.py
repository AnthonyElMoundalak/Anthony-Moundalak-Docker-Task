import requests

url = "http://localhost:5000/store"
data = {
    "name": "monkey.jpeg",
    "content": "./images.jpeg"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json)

