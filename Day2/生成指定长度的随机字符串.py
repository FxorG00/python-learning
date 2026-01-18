import string
import random
ALL=string.digits+string.ascii_letters
def generate(len) :
    """
    生成指定长度的一串随机字符串
    :return:
    """
    return ''.join(random.choices(ALL,k=len))
# '分隔符'.join([]) 将列表里面的元素用分隔符连接成一个字符串
# random.choices(列表，k），从列表里有放回地抽 k 个，返回一个列表
# ALL 是一个字符串，也可以认为是一个列表
for i in range(10,15) :
    print(generate(i))