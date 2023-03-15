
#https://api.publicapis.org/entries PUBLIC API
import requests



# parameter= {"amount":10,
#             "type:":"boolean"}


# question_data = requests.get("https://opentdb.com/api.php", params=parameter)
# question_data.raise_for_status()
# data = question_data.json()
# question_data = (data["results"])
# print(question_data)

API = "https://www.boredapi.com/api/activity"
reponse = requests.get(API)
reponse.raise_for_status()
data = reponse.json()
print(data["activity"])