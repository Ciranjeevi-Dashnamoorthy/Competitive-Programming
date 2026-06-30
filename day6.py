
n=int(input())
arr=list(map(int,input().split()))

from collections import Counter

d=Counter(arr)

keys=sorted(d.keys())

maxi=0
ones=0

for key in keys:
    
    val=key
    while d[val]>0:
        ct=d[val]
        if ct%2!=0:
            ones+=1
            maxi=max(maxi,val)

        carry=ct//2
        d[val]%=2
        if carry>0:
            val+=1
            d[val]+=carry
        else:
            break
print(maxi+1-ones)