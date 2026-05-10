import json
import random

import requests
import pandas as pd

url = "https://raw.githubusercontent.com/zgok/api_json_files/refs/heads/main/raw_json.json"
response= requests.get(url)
df=pd.json_normalize(response.json())
print(df.to_string(index=False))
first_names= pd.json_normalize(response.json())['name'].str.split().str[0].unique().tolist()
last_names= pd.json_normalize(response.json())['name'].str.split().str[1].unique().tolist()
cities= pd.json_normalize(response.json())['address.city'].unique().tolist()
emails= pd.json_normalize(response.json())['email'].unique().tolist()

users = []

for i in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"
    email = f"{first.lower()}{i}@mail.com"
    city = random.choice(cities)

    user = {
        "name": name,
        "email": email,
        "address": {
            "city": city
        }
    }

    users.append(user)

with open("page3.json", "w") as f:
    json.dump(users, f)