import time

# f = open(r'./其他/课程1.txt', 'r', encoding='utf-8')
# text = f.read()
# # print(text,type(text))
# count = text.count("itheima")
# print(count)
# f.close()

# f = open("D:/test.txt","w",encoding="utf-8")
# f.write("Hello World!!!")
# f.flush()
# time.sleep(600000)
# f.close()

# f = open("./其他/append写入.txt","a",encoding="utf-8")
# f.write("黑马程序员\n")
# f.close()

fr = open('./账单.txt','r',encoding='utf-8')
fw = open('./其他/账单备份.txt.bak','w',encoding='utf-8')
for line in fr:
    line = line.strip()
    if line.split(',')[4] == "测试":
        continue
    fw.write(line)
    fw.write("\n")
fr.close()
fw.close()
