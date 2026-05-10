import requests

response = requests.get("https://api.github.com")

print("Status:", response.status_code)
print("Server:", response.headers.get("Server"))
