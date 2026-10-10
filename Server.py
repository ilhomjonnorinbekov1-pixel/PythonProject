import requests
url = f"https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 41.2995,
    "longitude": 69.2401,
    "current": "temperature_2m"
}
try:
    r = requests.get(url, params = params, timeout=5)
    r.raise_for_status()

    data = r.json()
    harorat = data["current"]["temperature_2m"]

    print(f"Toshkent ob-xavosi : {harorat} gradus")

    if harorat < 10:
        print("Tashqari issiq ! ")

    elif harorat > 40:
        print("Xavo juda issiq ! ")

    else:
        print("OB-Xavo juda yaxshi ")

except requests.ConnectionError:
    print("Malumot olishda xatolik yuz berdi ")


import requests
import json
from datetime import datetime

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
r = requests.get(url)

if r.status_code == 200:
    valyuta = r.json()

    kurslar = {}

    for i in valyuta:
        if i["Ccy"] in ["USD", "EUR", "RUB"]:
            kurslar[i["Ccy"]] = float(i["Rate"])


    sana = datetime.now().strftime("%Y-%m-%d")

    yangi_info = {
        "sana" : sana,
        "USD" : kurslar["USD"],
        "EUR" : kurslar["EUR"],
        "RUB" : kurslar["RUB"]
    }

    try:
        with open("kurslar.json", "r") as file:
            malumotlar = json.load(file)

    except FileNotFoundError:
        malumotlar = []

    malumotlar.append(yangi_info)

    with open("kurslar.json", "w") as file:
        json.dump(malumotlar, file , indent=4)

    print("Kursla saqlandi ! ")
    print(yangi_info)

else:
    print(f"Apida  nmadur xatolik bor >>> {r.status_code}")






































