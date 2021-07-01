from collections import deque
def dfs(i):
	queue = deque([i])
	while queue:
		ele = queue.popleft()
		if visited[ele] is False:
			for friend in graph[ele]:
				if visited[friend] is False:
					queue.append(friend)
		visited[ele] = True

n, m = map(int, input().split())
gold = sorted(zip(map(int, input().split()), range(n)))
graph = [[] for _ in range(n)]
for i in range(m):
	a,b = map(int, input().split())
	graph[a-1].append(b-1)
	graph[b-1].append(a-1)
visited = [False]*n
ans = 0
for i in range(n):
	a,b = gold[i]
	if visited[b] is False:
		dfs(b)
		ans += a
print(ans)
