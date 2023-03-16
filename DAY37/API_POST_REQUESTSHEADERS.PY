# ADVANCED AUTHENTICATION AND POST/PUT/DELETE REQUESTS

""""  
HTTP REQUESTS:
GET  requests.get()
POST requests.post()
PUT  requests.put()
DELETE requests.delete() """

# import os
import requests 
from datetime import datetime


token = "12345678abcd"   #os.environ.get("token")
username = "pixela-rdm"
id = "pixel-graph-abc"


#----------1--setup user account-----------------------------#
pixela_endpoint = "https://pixe.la/v1/users"

user_params = { 
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response=requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)

#--------------2--- advanced authentication using an HTTP header ---------------#
# #Create a graph definition
graph_endpoint= f"{pixela_endpoint}/{username}/graphs"

graph_config ={
    "id":id,
    "name": "cycling graph",
    "unit":"km",
    "type": "float",
    "color":"ajisai"
}

header = {
    "X-USER-TOKEN":token
}

# response= requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

#-----------------------3--Get the graph!-------------------------------------------
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph 
#my_page = https://pixe.la/v1/users/pixela-rdm/graphs/pixel-graph-abc.html 

#-------------------------4--Post value to the graph---------------------------

post_value = f"{pixela_endpoint}/{username}/graphs/{id}"

today = datetime(year=2023, month=3 , day= 14)
#print(today.strftime("%y/%m/%d"))


post_config= {
    "date": "20221010", # or today.strftime("%Y%m%d")
    "quantity": "4.32",
}

# response=requests.post(url=post_value, json=post_config, headers=header)
# print(response.text) # then we need to reload the pag to watch the changes.

#--------------------5---update data wit put -----------------------------------------
update_requests = f"{pixela_endpoint}/{username}/graphs/{id}/{20221010}"

put_dict = {
    "quantity":"35.23",
    
}

# response=requests.put(url=update_requests, json=put_dict, headers=header)
# print(response.text)

#------------------6--DELETE DATA---------------------------

# it is not necesary the other previos parameter 
delete_requests = f"{pixela_endpoint}/{username}/graphs/{id}/{20221010}"

response=requests.delete(url=delete_requests,headers=header)
print(response.text)
