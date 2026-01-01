import re
r"""
.  匹配除换行符以外的任意字符
\w 匹配字母，数字或下划线
\s 匹配任意的空格符（较少）
\d 匹配数字
\n 匹配一个换行符（较少）
\t 匹配一个制表符（较少）

^\d 匹配字符串的开始
$\d 匹配字符串的结尾

\W 匹配非字母，数字或下划线（较少）
\D 匹配非数字（较少）
\S 匹配非空白符（较少）
a|b 匹配字符a或字符b
() 匹配括号内的表达式，也表示一个组
[...] 匹配字符组中的字符 例如：[a-zA-Z0-9_]
[^...] 匹配非字符串中的字符

\d* 重复零次或更多次
\d+ 重复一次或更多次
\d? 重复零次或一次
\d{n} 重复n次
\d{n,} 重复n次或更多次
\d{n,m} 重复n到m次

.* 贪婪匹配
.*? 惰性匹配
"""

#返回列表
lst = re.findall(r"\d+","我的电话号是：10086,stella的电话号是：10010")
print(lst)

#返回迭代器
it = re.finditer(r"\d+","我的电话号是：10086,stella的电话号是：10010")
for i in it:
    print(i.group())

#返回match对象，用group取出
s = re.search(r"\d+","我的电话号是：10086,stella的电话号是：10010")
print(s.group())

# #从头开始匹配
# s = re.match(r"\d+","我的电话号是：10086,stella的电话号是：10010")
# print(s.group())

# 预加载正则表达式
obj = re.compile(r'\d+')
ret = obj.finditer("我的电话号是：10086,stella的电话号是：10010")
for i in ret:
    print(i.group())

ret = obj.findall("你是真的666")
print(ret)

s = """
<div class=‘jay’><span id='1'>郭麒麟</span></div>
<div class=‘jj’><span id='2'>宋铁</span></div>
<div class=‘jolin’><span id='3'>大聪明</span></div>
<div class=‘sylar’><span id='4'>范思哲</span></div>
<div class=‘tory’><span id='5'>胡说八道</span></div>
"""

#（?P<分组名字>正则)单独提取内容
obj = re.compile(r"<div class=‘.*?’><span id='(?P<id>\d)+'>(?P<data>.*?)</span></div>",re.S) # re.S：让点能匹配换行符
result = obj.finditer(s)
for i in result:
    print(i.group("id"),end=".")
    print(i.group("data"))
