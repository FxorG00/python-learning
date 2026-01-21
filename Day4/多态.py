# 多态：多种状态
# 完成某个行为的时候，调用不同的子对象会得到不同的状态
# 父类：抽象类：有抽象方法（接口）
# 子类，去具体实现这些接口
# 鸭子类型：其实，只要有 speak 这个方法，就可以传入到 make_noise
class Animal :
# 相当于一个顶层设计
    def speak(self) :
        pass
    # 带 pass 的就是抽象方法
# 带抽象方法的就是抽象类
class Dog(Animal) :
    # 子类是继承父类的，所以有 speak 这个方法
    # 但是 speak 被复写了，所以会调用 speak 的时候调用的是子类的
    def speak(self) :
        print('汪汪汪')
class Cat(Animal) :
    def speak(self) :
        print('喵喵喵')
def make_noise(animal) :
    animal.speak()
# 同一个行为，传入不同的对象，得到的状态不同
# 函数形参：父类
# 函数传入子类
dog=Dog()
cat=Cat()
make_noise(dog)
make_noise(cat)
