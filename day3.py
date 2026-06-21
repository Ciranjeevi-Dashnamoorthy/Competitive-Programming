

"""

350C-Bombs

"""
n=int(input())
arr=[]


total=0
for _ in range(n):
    x,y=map(int,input().split())
    arr.append([abs(x)+abs(y),x,y])
    if x!=0:
        total+=2
    if y!=0:
        total+=2
    total+=2
print(total)


arr.sort()

for _,x,y in arr:

    if x>0:
        print(1,x,"R")
    elif x<0:
        print(1,-x,"L")
    if y>0:
        print(1,y,"U")
    elif y<0:
        print(1,-y,"D")
    
    print(2)
    if x>0:
        print(1,x,"L")
    elif x<0:
        print(1,-x,"R")
    if y>0:
        print(1,y,"D")
    elif y<0:
        print(1,-y,"U")
    print(3)






