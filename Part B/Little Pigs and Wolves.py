n,m = map(int, input().split())
arr = []
for i in range(n):
	arr.append(list(input()))
ans = 0
s = set()
for i in range(n):
	for j in range(m):
		if arr[i][j] == 'P':
			if i>0:
				if arr[i-1][j] == 'W' and (i-1,j) not in s:
					s.add((i,j))
					continue
			if j>0:
				if arr[i][j-1] == 'W' and (i,j-1) not in s:
					s.add((i,j-1))
					continue
			if i<n-1:
				if arr[i+1][j] == 'W' and (i+1,j) not in s:
					s.add((i+1,j))
					continue
			if j<m-1:
				if arr[i][j+1] == 'W' and (i,j+1) not in s:
					s.add((i,j+1))
					continue

print(len(s))