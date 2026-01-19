class Student :
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def study(self,course_name) :
        print(f"{self.name}在学习 {course_name}")
    def play(self) :
        print(f"{self.age}岁的学生们在玩")
Stu1=Student('小红',18)
Stu2=Student('小明',20)
Stu1.study('语文')
Stu2.play()
Stu3=Stu1
print(Stu1)
print(Stu2)
print(Stu3)
