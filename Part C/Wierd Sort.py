t = int(input())
for _ in range(t):
	n,m=map(int, input().split())
	a=list(map(int, input().split()))
	p=list(map(int, input().split()))
	p=set(p)
	while(1):
	    f=0
	    for i in range(n-1):
	        if a[i]>a[i+1] and i+1 in p:
	            a[i],a[i+1]=a[i+1],a[i]
	            f=1
	    if not f:
	        break
	if a==sorted(a):
	    print("YES")
	else:
	    print("NO")
