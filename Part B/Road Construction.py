n,m=map(int,input().split())
L=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    L[a-1]=-1
    L[b-1]=-1
central=0
for i in range(n):
    if L[i]==0:
        central=i+1
        break
print(n-1)
for i in range(1,n+1):
    if i!=central:
        print(central,i)
