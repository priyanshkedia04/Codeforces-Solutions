n=int(input())
A=[int(input()) for i in range(n)]
r=0
for i in range(n):
    c=0
    while i>=0:
        i=A[i]-1
        c=c+1
    r=max(r,c)
 
 
print(r)