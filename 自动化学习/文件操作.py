f = open("./其他/test1.txt","r",encoding="utf-8")
print(type(f))
# print(f"读取十个字节的结果：{f.read(10)}")
# lines = f.readlines()
# print(f"lines对象的内容是：{lines}")

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行的数据是：{line1}")
# print(f"第二行的数据是：{line2}")
# print(f"第三行的数据是：{line3}")

for line in f:
    print(f"每一行的数据是：{line}")
f.close()
