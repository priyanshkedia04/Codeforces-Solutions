n,m=map(int,input().split())
l=list(map(int,input().split()))
l.insert(0,0)
i=1
while(i<m):
	i+=l[i]
 
 
if(i==m):
	print("YES")
else:
	print("NO")
