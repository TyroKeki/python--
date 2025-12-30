import csv

data = [
    ["date", "province", "sales"],
    ["2011-01-01", "广东省", 1689],
    ["2011-01-01", "湖南省", 2353]
]

with open("qwen_output.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)


"""读入二元列表"""
# 要写入的数据
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

# 打开 CSV 文件
with open('data.csv', mode='w', encoding='utf-8', newline='') as file:
    # 创建 csv.writer 对象
    csv_writer = csv.writer(file)

    # 写入数据
    for row in data:
        csv_writer.writerow(row)

# 打开 CSV 文件
with open('data.csv', mode='r', encoding='utf-8') as file:
    # 创建 csv.reader 对象
    csv_reader = csv.reader(file)

    # 逐行读取数据
    for row in csv_reader:
        print(row)


"""csv读入字典"""
data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
]

with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # 写入表头
    csv_dict_writer.writeheader()

    # 写入数据
    for row in data:
        csv_dict_writer.writerow(row)

data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
]

with open('data.csv', mode='r', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file)

    for row in csv_dict_reader:
        print(row)