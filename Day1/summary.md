# 2026/1/16 结束 [1,11]
```
没有 i++,++i，只有 i+=1
i**2 是 i^2
i//2 是 i/2 然后下取整，返回一个 int
input() 是读取一整行，然后返回一个字符串
```
```python
# 修改后的代码
a = []
n = int(input())

# 修改这一行：一次性读取一行，然后分割为多个数字
numbers = input().split()  # 将输入按空格分割成字符串列表
for num_str in numbers:
    a.append(int(num_str))  # 将每个字符串转换为整数

# 或者更简洁的写法：
# a = list(map(int, input().split()))

# 后续的统计逻辑保持不变
for i in range(0, n):
    ans = 0
    for j in range(0, i):
        if a[j] < a[i]:
            ans += 1
    print(ans, end=" ")
```