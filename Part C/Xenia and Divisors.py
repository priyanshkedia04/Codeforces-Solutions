n=int(input())
 
a=list(map(int,input().split()))
 
p=a.count(1)
q=a.count(2)
r=a.count(3)
s=a.count(4)
t=a.count(6)
 
if (p==n//3 and q+r==n//3 and s+t==n//3 and s<=q and t>=r):
 
    for i in range(r):
 
        print(1,3,6)
 
    for i in range(s):
 
        print(1,2,4)
 
    for i in range(t-r):
 
        print(1,2,6)
 
else:
 
    print(-1)