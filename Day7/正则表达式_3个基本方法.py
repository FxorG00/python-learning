import re
s="1python itheima python"
# match 是只能从开头开始，没有就寄了
result=re.match("python",s)
print(result)
# print(result.span())
# print(result.group())
# search 是在整个字符串中找第一个能匹配的
result=re.search("python",s)
print(result)
# findall 找到全部匹配成功的
result=re.findall('python',s)
print(result)

