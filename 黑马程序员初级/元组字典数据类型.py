"""字符串"""
my_str = "itheima and itcast"

value  = my_str[2]
value2 = my_str[-16]
print(value, value2,sep="|")

value = my_str.index("and")
print(value)

new_my_str = my_str.replace("it","程序",100)
print(new_my_str)

my_str = "hello python itheima  itcast"
my_str_list = my_str.split(" ")
print(my_str_list)

my_str = "   itheima and itcast   \n  "
new_my_str = my_str.strip()
print(new_my_str)

count = new_my_str.count("it")
print(count)

num = len(new_my_str)
print(num)

"""集合"""
my_set = {"传智教育","黑马程序员","itheima","itheima",1,2,3}
my_set.add("python")
print(f"{my_set}")

my_set.remove("黑马程序员")
print(f"{my_set}")

element = my_set.pop()
print(f"{my_set}，被取出的是：{element}")

my_set.clear()
print(f"{my_set}")

set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2) # 取差集
print(set3)

"""字典"""
my_dict = {
    "王力宏":99,
    "周杰伦":88,
    "林俊杰":77,
}

score = my_dict["王力宏"]
print(score)

my_dict["张学友"] = 66
my_dict["周杰伦"] = 11
score = my_dict.pop("周杰伦")
print(f"被移除的分数是{score}")

keys = my_dict.keys()
print(f"所有的key: {keys},注意类型为：{type(keys)}")

# for key in keys: # 等价
for key in my_dict:
    print(f"字典的key是{key}")
    print(f"字典的value是{my_dict[key]}")

result = my_dict.get("周杰伦")
print(f"我用get方法取到{result}")

result = my_dict.popitem()
print(f"弹出最后一个{result}")
print(f"还剩下{my_dict}")

my_dict["张学友"] = 66
my_dict["周杰伦"] = 11

total_score = my_dict.values()
print(f"一共有成绩{total_score},{type(total_score)}")

all_thing = my_dict.items()
print(f"一共有键值对{all_thing},{type(all_thing)}")

