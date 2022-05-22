import requests

x = requests.get('https://gorest.co.in/public/v2/users')

print(x.text)