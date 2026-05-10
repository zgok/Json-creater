import json
import random

first_names = ["ERVIN","LEANNE","KURTIS","GLENNA","PATRICIA","CHELSEY","CLEMENTINE","CLEMENTINA","MRS.","NICHOLAS"]
last_names = ["HOWELL","GRAHAM","WEISSNAT","REICHERT","LEBSACK","DIETRICH","BAUCH","DUBUQUE","DENNIS SCHULIST","RUNOLFSDOTTIR V"]
cities = ["Wisokyburgh","Gwenborough","Howemouth","Bartholomebury","South Elvis","Roscoeview","McKenziehaven","Lebsackbury","South Christy","Aliyaview"]
emails=["Chaim_McDermott@dana.io","Julianne.OConner@kory.org","Karley_Dach@jasper.info","Lucio_Hettinger@annie.ca","Nathan@yesenia.net","Rey.Padberg@karina.biz","Shanna@melissa.tv"]

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

with open("page1.json", "w") as f:
    json.dump(users, f)