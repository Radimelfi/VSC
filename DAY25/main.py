with open ("weather_data.csv") as data:
   data_file = data.readlines()
   print(data_file)


import csv
 
with open ("weather_data.csv" ) as data:
    data_file = csv.reader(data)
    print(data_file)

    for temp in data_file:
        print (temp)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])


#PRACTICING DIFERRENT METHOD
data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print (data_list)

average = round(data["temp"].mean(),2)
print(average)

maximun = data["temp"].max()
print(maximun)


 # GET DATA IN COLUMNS #

print (data["condition"]) 
print(data.day)

# GET DATA IN ROW 
print (data[data.day == "Monday"].max())
print (data[data.temp == data.temp.max ()])

#  CREATE A DATAFRAME FROM SCRATCH 
DICT = {
    "student": ["Any", "Radi", "Randy"],
    "score": [85, 96, 89]
}

data_F = pandas.DataFrame(DICT)
print(data_F)
data_F.to_csv("Score.csv")


