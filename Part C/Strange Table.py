for i in range(int(input())):
	n,m,x = map(int, input().split())
	row = x%n
	if row == 0:
		row = n
	col = x//n if x%n == 0 else x//n + 1
	ans = row*m - (m-col)
	print(ans)
