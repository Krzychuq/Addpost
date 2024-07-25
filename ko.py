import requests
import base64

from facepy import GraphAPI
import json

# configuration
wordpress_user = "<username>"
wordpress_password = "XXXX XXXX XXXX XXXX XXXX XXXX"
wordpress_credentials = wordpress_user + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credentials.encode())
wordpress_header = {'Authorization': 'Basic ' + wordpress_token.decode('utf-8')}



# fuction to create post 
def nowy_post(tytul, tresc, d):
    uproszczona_nazwa = tytul.strip()
    uproszczona_nazwa = uproszczona_nazwa.replace(" ", "-")
    api_url = '' # https://example.com/wp-json/wp/v2/posts
    data = {
    'date' : d,
    'title' : tytul,
    'status': 'publish',
    'slug' : uproszczona_nazwa,
    'content': tresc,
    'categories': '2'
    }
    response = requests.post(api_url,headers=wordpress_header, json=data)
    print(response)
# IN LOG: response 201 CORRECT // 200 FAILED

# DATA to post
title = []
content = []
daty = [] # 2024-01-16T08:00:00 (daty example)

# loop
numer = 0
while numer < len(title):
    # add data to wordpress site
    nowy_post(title[numer], content[numer], daty[numer])
    numer += 1