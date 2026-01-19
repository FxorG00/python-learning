my_dict=dict()
n=int(input())
ans=0
for i in range(0,n) :
    str=input()
    # print(str in my_dict)
    if str not in my_dict :
        my_dict[str]=1
        ans+=1
print(ans)

