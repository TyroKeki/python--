mylist = ["itcast","itheima","python"]
index = mylist.index("itheima")
print(index)

mylist[0] = "传智教育"
mylist2 = ["""ll'""'ll"""]
print(mylist2)

mylist.insert(1,"best")
mylist.append("黑马程序员")

mylist2 = [1,2,3]
mylist = mylist + mylist2
print(mylist)

del mylist[0]
print(mylist)

element = mylist.pop(0)
print(element)

mylist = [1,2,3,3,2,1]
mylist.remove(1)
print(mylist)

mylist.clear()
print(mylist)

mylist = [1,2,3,3,2,1,2,2]
count = mylist.count(2)
print(count)


import copy
original = [1, 2, 3, 4, 5]

copy1 = original.copy()
copy2 = original[:]          # 切片复制
copy3 = list(original)
copy4 = copy.copy(original)

copy1.append(6)
copy2.append(7)
copy3.append(8)
copy4.append(9)

print(original)