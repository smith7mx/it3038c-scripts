import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=f3d255b1085377a6d1cfe21245038909' % zip)
data=r.json()
print(data['weather'][0]['description'])