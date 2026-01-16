a=[]
n=int(input())
numbers=input().split()
for i in range(0,n) :
    a.append(int(input()))
for i in range(0,n) :
    ans=0
    for j in range(0,i) :
        if a[j]<a[i] :
            ans+=1
    print(ans,end=" ")