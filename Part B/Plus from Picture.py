def dfs(x,y):
	queue = [(x,y)]
	while queue:
		x,y = queue.pop()
		if (x,y) in visited:
			continue
		visited.add((x,y))
		if len(visited) > r+c-1:
			print('NO')
			exit()
		x_points[x] = x_points.get(x,0) + 1 
		y_points[y] = y_points.get(y,0) + 1
		for k in range(4):
			nrow = x + rows[k] 
			ncol = y + cols[k]
			if 0<=nrow<r and 0<=ncol<c and (nrow, ncol) not in visited:
				if graph[nrow][ncol] == '*':
					queue.append((nrow, ncol))

r,c = map(int, input().split())
rows = [-1,1,0,0]
cols = [0,0,-1,1]
graph = []
for i in range(r):
	graph.append(input())

visited = set()
x_points, y_points = {},{}
count = 0

for i in range(r):
	for j in range(c):
		if graph[i][j] == '*' and (i,j) not in visited:
			if count == 1:
				print('NO')
				exit()
			dfs(i,j)
			count += 1
if len(visited) > r+c-1 or count == 0:
	print('NO')
	exit()

mx = sorted(x_points.items(), key = lambda x: x[1])[-1][0]
my = sorted(y_points.items(), key = lambda x: x[1])[-1][0]

vertical, horizontal = 0,0

for i in visited:
	if i[0] == mx:
		vertical += 1
	if i[1] == my:
		horizontal += 1

if horizontal + vertical - 1 != len(visited):
	print("NO")
	exit()

if (mx+1,my) in visited and (mx-1,my) in visited and (mx,my+1) in visited and (mx,my-1) in visited:
	print('YES')
else:
	print('NO')