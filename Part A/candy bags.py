n = int(input())
arr = [[i, n**2 - (i-1)] for i in range(1, (n**2)//2 + 1)]
for i in range(0,(n**2)//2, n//2):
	ans = []
	temp = arr[i:i+n//2]
	for j in temp:
		ans.extend(j)
	print(*ans)