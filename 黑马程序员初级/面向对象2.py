class Student:
    name = None
    age = None
    tel = None

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student创建了一个类对象")

    def __str__(self):
        return f"student类对象，name: {self.name}, age: {self.age}, tel: {self.tel}"

    def __le__(self,other): #le 小于等于，lt 小于
        return self.age <= other.age

stu1 = Student("周杰伦",31,"1850006")
stu2 = Student("周杰伦",41,"1850006")
print(str(stu1))
sts = (stu1<=
       stu2)
print(sts)