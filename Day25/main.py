import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
temp_list = data["Primary Fur Color"].to_list()


gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnemon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnemon_squirrels_count)
print(black_squirrels_count)

data_dict = {"Fur Color": ["Gray", "Cinnemon", "Black"], "Count": [gray_squirrels_count, cinnemon_squirrels_count, black_squirrels_count]}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squrrel_data.csv")

