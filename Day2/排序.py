n=int(input())
numbers=input().split()
a=[]
for i in numbers :
    a.append(int(i))
a=sorted(a)
for i in a :
    print(i,end=" ")

