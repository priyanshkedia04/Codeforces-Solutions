n, t = map(int, input().split())
a= list(map(int,input().split()))
i,s,j= 0,0,0
for i in range(n):
    s+=a[i]
    if s>t:
        s-=a[j]
        j+=1
print(n-j)