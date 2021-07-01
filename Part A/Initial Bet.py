arr = list(map(int, input().split()))
s = sum(arr)
if s%5 == 0:
	if s//5 > 0:
		print(s//5)
		exit()
	
print(-1)