class Student :
    def __init__(self,name,age,add) :
        self.name=name
        self.age=age
        self.add=add
    def __str__(self) :
        return f"我调用了 str 函数，这个对象是 {self.name}"
    def __lt__(self, other) : # less than 小于
        return self.age<other.age
    def __le__(self, other) :
        return self.age<=other.age
    def __eq__(self, other) :
        return self.age==other.age
a=list()
for i in range(1,3) :
    print(f"当前录入第 {i} 位学生信息")
    print("请输入学生姓名: ",end='')
    name=input()
    print("请输入学生年龄: ",end='')
    age=int(input())
    print("请输入学生地址： ",end='')
    add=input()
    nw=Student(name,age,add)
    a.append(nw)
    print(f"学生 {i} 信息录入完成，信息为：{name},{age},{add}")
print(a[0])
print(a[1])
print(a[0]<a[1])
print(a[0]==a[1])
print(a[0]>=a[1])