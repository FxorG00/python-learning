class Phone :
    name='xiaomi'
    __siyou=1
    def call_by_4g(self) :
        print('4g通话')
    def __say_hi(self) :
        print('hi')
# 私有的东西没办法继承
class Phone2025(Phone) :
    def __say_hello(self) :
        print('hello')
    def call_by_5g(self) :
        print('5g通话')
        self.__say_hello()

my_Phone=Phone2025()
my_Phone.call_by_5g()