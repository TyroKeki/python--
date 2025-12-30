class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self):
        print(f"Hi大家好，我是{self.name}")

    def say_hi2(self,msg):
        print(f"Hi大家好，我是{self.name},{msg}")

stu1 = Student()
stu1.name = "林俊杰"
stu1.gender = "男"
stu1.nationality = "中国"
stu1.native_place = "山东省"
stu1.age = 31

stu2 = Student()
stu2.name = "周杰伦"

stu1.say_hi2("不错you")
stu2.say_hi2("看好ni")
