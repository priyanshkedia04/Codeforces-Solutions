for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	ans = []
	root = arr[0]
	visited = [False]*n
	visited[0] = True
	temp = 0
	for i in range(1,n):
		if arr[i] != root:
			ans.append([1, i+1])
			visited[i] = True
			temp = i
	if len(ans) == 0:
		print('NO')
		continue
	for i in range(n):
		if visited[i] is False:
			ans.append([temp+1, i+1])
	print('YES')
	for i in ans:
		print(*i)

