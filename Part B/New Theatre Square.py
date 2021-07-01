for i in range(int(input())):
	n,m,x,y = map(int, input().split())
	arr = []
	for i in range(n):
		arr.append(list(input()))
	pairs = 0
	cost = 0
	for i in range(n):
		for j in range(m):
			if arr[i][j] == '.':
				if j+1 < m:
					if arr[i][j+1] == '.':
						arr[i][j], arr[i][j+1] = '*', '*'
						pairs += 1
					else:
						cost += x
				else:
					cost += x
	print(min(cost + pairs*2*x, cost + pairs*y))