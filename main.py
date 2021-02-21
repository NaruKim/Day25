# with open('weather_data.csv') as file1:
#     data = file1.readlines()
#     for i in range(len(data)-1):
#         data[i] = data[i].strip()
#
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     header = next(data)
#     temperature = []
#     print(data)
#     for row in data:
#         # if row[1] != 'temp':
#         temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(type(data['temp']))
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# data_list = data['temp'].to_list()
# print(data_list)
#
# average = data['temp'].mean()
# print(average)

#똑같은 애들 =====

# average = sum(data_list) / len(data_list)
# print(average)

# total = 0
# for i in data['temp']:
#     total += i
# total /= len(data_list)
# total = round(total)
# print(total)

#===============================

# high = data['temp'].max()
# print(high)
#
# print(data['condition'])
# print(data.condition)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# print("------------------------------------")
# monday = data[data.day == "Monday"]
# temp = monday.temp
# temp = temp*9/5+32
# print(temp)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# # Squirrel_count 만들기 ========================
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#
# gray_number = 0
# red_number = 0
# black_number = 0
#
# for i in data['Primary Fur Color']:
#     if i == 'Gray':
#         gray_number += 1
#
# print(gray_number)
#
# for i in data['Primary Fur Color']:
#     if i == 'Cinnamon':
#         red_number += 1
#
# print(red_number)
#
# for i in data['Primary Fur Color']:
#     if i == 'Black':
#         black_number += 1
#
# print(black_number)
#
# new_data = {
#     "Fur Color": ['gray', 'red', 'black'],
#     "Count": [gray_number, red_number, black_number],
# }
#
# new_data_DataFrame = pandas.DataFrame(new_data)
# print(new_data_DataFrame)
# new_data_DataFrame.to_csv('squirrel_count.csv')
#===========================================================

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count_MK2.csv')