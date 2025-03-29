import requests
response = requests.get('https://scratch.mit.edu/')
print(response.content)