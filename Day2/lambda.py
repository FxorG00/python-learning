numbers = [1, 2, 3, 4, 5, 6]
# 用一行代码实现：筛选奇数，然后加10
result = list(map(lambda x: x+10, filter(lambda x: x%2==1, numbers)))
# 结果应该是：[11, 13, 15]
print(result)