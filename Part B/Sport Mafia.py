n,k = map(int, input().split())
l = 0
r = n
while l<=r:
	m = (l+r)//2
	val = m*(m+1)//2 - (n-m)
	if k == val:
		print(n-m)
		exit()
	elif k > val:
		l = m+1
	else:
		r = m-1
