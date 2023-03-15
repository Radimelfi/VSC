# API KEYS, Authentication, Environment Variables and Sending SMS 
import requests

repon= "https://api.openweathermap.org/data/3.0/onecall"
api_key = "bc4d6705c232e418ca45ece3be9d92a7"

weather_param= {
    "lat" : 51.507351,
"lon" : -0.127758,
"appid":api_key,
}

response= requests.get(repon, params=weather_param)
print(response.status_code)



# twilio API Send email  pythonanywhere
 