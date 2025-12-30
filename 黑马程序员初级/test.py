# print(f"字符串大小比较:{'abc'>'bb'}")
#
# a = map(int,input().split())
# print(a,type(a))
# b1 = next(a)
# print(b1)
# b2 = next(a)
# print(b2)
#
# import json
# s = [{'name1':  'zhangsan','addr'  :  "jiangsu"},{"name1":'lisi','addr':'nanjing'},{'name1':'wangwu','addr':'wuxi'}]
# json_str = json.dumps(s)
# print(type(json_str))
# print(json_str)
#
# li = json.loads(json_str)
# print(type(li))
# print(li)
#
# if li == s:
#     print('即使s格式奇怪，依然等价')
# else:
#     print('不等价')
#
# jihe = set('abcdefghij')
# print(jihe)
#
# char = "和黑马程序员"
# print(char,"一起学python",sep='')
# print(char + "一起学python")
#
# # matrix = [[0]*5 for i in range(5)]
# print(char*2+"一起学python\t")
#
# char = "New York 1999"
# result = char.rsplit(maxsplit=1)[1]
# print(result)
#
#
# char = "加上波浪线后说话变得好慢呀"
# str_list = list(char)
# result = " ~ ".join(str_list)
# refined = result + " ~"
# print(refined)
#
# chars = "abc123"
# chars.replace("c","")
# print(chars)
#
# chars = "abcd"
# for i, char in enumerate(chars):
#     print((i,char))
#
# for tup in enumerate(chars):
#     print(tup)
#
# chars = "abcdef"
# for i,char in enumerate(chars):
#     print(f"目前字符{char}")
#     chars = chars[1:]
#     print(f"剩余部分：{chars}")
#
# n = 20
# for i in range(1,n,1):
# n -= 1
#     print(i,n)
#
# help(list.remove)

# from pyecharts.charts import Bar
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
# help(Bar)

# import turtle as tt
# # help(tt.forward)
# # print(dir(tt))
# help(tt.fillcolor)

# a =3.9415926
# b = int(a)
# print(b)

# import turtle
# help(turtle.Screen)

chars = "EF98"
newChars = int(chars,16)
print(newChars)