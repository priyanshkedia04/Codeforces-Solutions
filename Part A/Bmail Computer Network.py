n=int(input())
a=[0]*(n+1)
i=2
for s in input().split():
    a[i]=int(s)
    i+=1
ans=[n]
while True:
    n=a[n]
    if n==0:break
    ans.append(n)
print(*ans[::-1])
 