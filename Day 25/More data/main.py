import pandas as pd
data = pd.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")\

fur_colours = data.groupby("Primary Fur Color")
sizeofGroups = fur_colours.size()
print(sizeofGroups)
sizeofGroups.to_csv("Day 25/result.csv")
