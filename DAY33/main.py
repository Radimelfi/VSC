
import requests
from datetime import datetime

latitud = 18.733216
long = -70.162919

parameter = { "lat":latitud,
             "lng":long,
             "formatted":0,
             }

reponse= requests.get("https://api.sunrise-sunset.org/json", params=parameter)
reponse.raise_for_status()
data=reponse.json()
sunrise=int(data ["results"]["sunrise"].split("T")[1].split(":")[0])
sunset= int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)

time_now =datetime.now()
print(time_now.hour)