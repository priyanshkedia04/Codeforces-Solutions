n,k = map(int, input().split())
arr = [[0]*n for i in range(n)]
for i in range(n):
	arr[i][i] = k
for i in range(n):
	print(*arr[i])
