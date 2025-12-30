import csv

data = [[0]*9]*9

with open("数独数据输入接口.csv","w",encoding="utf-8-sig",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)