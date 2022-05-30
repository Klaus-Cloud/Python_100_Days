#import csv
#with open("Day 25/weather_data.csv") as file:
#    data = csv.reader(file)
#    temperatures =[]
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)


import pandas as pd 
data = pd.read_csv("Day 25/weather_data.csv")
##Dataframe to dictionary
#dataDict = data.to_dict()
#print(dataDict)

##Series to list
#temp_list =data["temp"].to_list()
#meanTemperature = sum(temp_list)/len(temp_list)

##Working with series
#average=data["temp"].mean()
#print(data["temp"].max())
#print(data.temp)

## Working with rows
#print(data[data.day == "Monday" ])
#print(data[data.temp == data.temp.max()])
#monday = data[data.day == "Monday"]
#print(monday.condition)
#print(int(monday.temp)*1.8 + 32)

#Creating DataFrame from scratch
data_dict ={
    "students":["Alette", "Iver", "Rook"],
    "scores": [7,8,9]
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv(".\Day 25\data.csv")