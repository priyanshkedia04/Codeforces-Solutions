a,b,n = map(int, input().split())
for i in range(0,10):
	if (10*a + i)%b == 0:
		print((10*a + i)*(10**(n-1)))
		exit()
print(-1)