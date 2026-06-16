n=int(input())

ans=1
while n%ans==0:
    ans*=3
print(n//ans +1)
