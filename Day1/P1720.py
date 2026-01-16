import math as m
n=int(input())
sq5=m.sqrt(5)
ans=m.pow((1+sq5)/2,n)-m.pow((1-sq5)/2,n)
ans=ans/sq5
print(f"{ans:.2f}")


