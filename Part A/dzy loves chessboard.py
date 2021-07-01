n,m = map(int, input().split())
s = list("WB"*(m//2) + 'W'*(m%2))
s_inv = list("BW"*(m//2) + 'B'*(m%2))
order = [s if i%2 == 0 else s_inv for i in range(n)]
inp = []
for i in range(n):
	inp.append(list(input()))
for i in range(n):
	for j in range(m):
		if inp[i][j] == '.':
			inp[i][j] = order[i][j]
		else:
			inp[i][j] = '-'
for i in range(n):
	print("".join(inp[i]))