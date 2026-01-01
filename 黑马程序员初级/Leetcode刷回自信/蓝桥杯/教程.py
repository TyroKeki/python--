# a = [0,1,2,3,4,5]
# for i in range(5):
#     print(hex(id(a[i])),end=" ")

# import sys
# lst = []
# for n in sys.stdin:
#     n = int(n)
#     lst.append(n)
# print(lst)

# 小数位
a = 1.114514
print(f"{a:.4f}")


rate1 = 0.133
rate2 = 0.5456
print(f"{rate1:.2%}, {rate2:.2%}")

# 时间输出
hh,mm,ss = 3,24,5
print(f"{hh:02d}:{mm:02d}:{ss:02d}")

# 千位分隔符
money = 123400114514
print(f"{money:,}")

# 科学记数法
num = 1145141919810
print(f"{num:.3e}")

# 左对齐、右对齐、居中对齐
left,middle,right = "左","中","右"
print(f"|{left:10}|")      # |左        |（默认左对齐）
print(f"|{right:>10}|")     # |        右|（右对齐）
print(f"|{middle:^10}|")     # |    中    |（居中对齐）
print(f"|{middle:*^10}|")    # |****中****|（用*填充）
hh,mm,ss = 3,24,5
print(f"{hh:0>2d}:{mm:0>2d}:{ss:0>2d}")

# 进制转换
n = 255
print(f"二进制：{n:b}")     # 11111111
print(f"八进制：{n:o}")     # 377
print(f"十六进制：{n:x}")   # ff（小写）
print(f"十六进制：{n:X}")   # FF（大写）
print(f"十进制：{n:d}")     # 255