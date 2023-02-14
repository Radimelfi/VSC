import pandas 

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_squierrels_count = len(data[data["Primary Fur Color"]== "Gray"])
Cinnamon_squierrels_count = len (data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"]== "Black"])

print (Gray_squierrels_count)
print (Cinnamon_squierrels_count)
print (black_squirrels_count )

dict_data = {"Primary Fur Color": ["Gray", "Cinnamon", "Black"],
              "cantidades de ardillas": [Gray_squierrels_count, Cinnamon_squierrels_count, black_squirrels_count]
}

DF = pandas.DataFrame(dict_data)
DF.to_csv("Squirrels_count.csv")