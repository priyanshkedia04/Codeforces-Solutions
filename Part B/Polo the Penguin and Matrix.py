n,m,d=map(int,input().split())
a=[]
for i in range(n):
    a+=(list(map(int,input().split())))
ans=0
a.sort()
mid=a[len(a)//2]
for i in a:
    x=abs(i-mid)
    if x%d!=0:
        print(-1)
        exit()
    ans+=x//d
print(ans)