import math as m
n=int(input())
ans=0
for i in range(1,n+1) :
    ans+=m.factorial(i)
print(ans)