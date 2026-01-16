def max(a,b) :
    if a>b :
        return a
    else :
        return b

n=int(input())
ans=0
i=2
while i**2<=n :
    if n%i==0 :
        ans=max(i,n//i)
        break
    i+=1
print(ans)