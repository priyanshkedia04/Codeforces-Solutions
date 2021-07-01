n = int(input())
arr = []
for _ in range(n):
	arr.append(list(map(int, input().split())))
ans = 0
visited = [False for i in range(n)]

def dfs(v):
	visited[v] = True
	for j in range(n):
		if visited[j] is False:
			if arr[j][0] == arr[v][0] or arr[j][1] == arr[v][1]:
				dfs(j)


# COUNT NUMBER OF UNCONNECTED COMPONENETS IN AN UNDIRECTED GRAPH
ans = 0
for i in range(n):
	if not visited[i]:
		dfs(i)
		ans += 1
print(ans-1)