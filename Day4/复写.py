# 对父类的属性、方法进行重写
# 直接写个同名的，就覆盖了
# super().属性/方法 去调用父类的东西
# 任何属性/方法在访问的时候一定是 对象+.
class Phone :
    name='huawei'
    def call_by_5g(self) :
        print('this is father')
class Phone2026(Phone) :
    name='xiaomi'
    def call_by_5g(self) :
        print('this is son')
        super().call_by_5g()
my_Phone=Phone2026()
my_Phone.call_by_5g()