# 类型注解只是用来提示你这个变量是什么类型而已
# Union 用于定义联合类型注释
# 变量名+：注解这个变量的类型
from typing import Union
def add(a:int,b:int)-> int :
# -> 这个函数的返回类型
    print(a+b)
var_1: int =123
print(var_1)
add(12,23)
my_list:list[Union[str,int]]=['hi',12,23]
print(my_list)