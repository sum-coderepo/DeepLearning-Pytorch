import time
import requests
import os

def ping():
    instance = os.getenv('WEBSITE_INSTANCE_ID', 0)
    url = 'https://sumeetstreamlitapp.azurewebsites.net'
    cookies = dict(ARRAffinity=instance)
    r = requests.get(url, cookies=cookies)
    print('OK')

while True:
    ping()
    time.sleep(180)