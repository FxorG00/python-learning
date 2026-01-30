import re
s='ith####eim@@a 233F4A nihao42 !!!24133'
result=re.findall(r'[A-Za-z!]',s)
print(result)
# 所谓正则表达式其实就是类似于通配符的东西，啥都能匹配
# findall 会对于每个括号都去找
# 匹配邮箱 ab-cd.123.def@qq/163/gmail.com.cn.a.b.1.3.c
# 所谓的分组匹配就是解决了之前只能一个一个字符匹配，把这些字符捆绑到一起
# ^ 意味着第一个字符一定要匹配，也就是只考虑前缀
# $ 最后一个一定要，两个都存在意味着只能对整个字符串匹配；
# ([\w-]+\.) 意味着 asfa123312412. 这种，捆绑起来，\. 匹配点自己
# 这样后面的 * 是作用于这一坨上面的
# (qq|163|gmail) 就是三个作为一个分组绑在一起，然后三个任选一个
r=r'^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$'
s='3320987642.abc.ABC._dfsss@163.com.cn.d-ffs'
result=re.search(r,s)
print(result)
s='3320987642.qwqf@qq.com.cn.asf'
# s=('3320987642@qq.com')
result=re.match(r,s)
print(result)
