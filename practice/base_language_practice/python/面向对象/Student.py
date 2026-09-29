class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def listen(self):
        print("有耳朵")
        return "有两只耳朵"

    def speak(self):
        print("有嘴巴")
        return "有一个嘴巴"

# python  的类中函数  打印这个函数的时候 也会连同打印他的返回值
# 如果没有 return 的情况下  他就会打印None

stu1 = Student("小敏",18)

stu1.high = 170
# print(stu1.high)
# print(stu1.name)
# print(stu1.age)
# print(stu1.listen())
# print(stu1.speak())
del stu1.high
for key, value in stu1.__dict__.items():
    print(key, value)