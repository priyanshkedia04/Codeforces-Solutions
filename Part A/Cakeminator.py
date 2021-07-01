r,c = map(int, input().split())
arr = []
rows = 0
cols = 0
for i in range(r):
	arr.append(input())
for i in range(r):
	if 'S' not in arr[i]:
		rows += 1
for i in range(c):
	temp = 0
	for j in range(r):
		if arr[j][i] != 'S':
			temp += 1
	if temp == r:
		cols += 1
print(rows*c + cols*r - rows*cols)