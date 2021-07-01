n,t = map(int, input().split())
if n == 1 and t == 10:
	print(-1)
elif t < 10:
	print(int('1'*n)*t)
else:
	print(int('1' + '0'*(n-1)))