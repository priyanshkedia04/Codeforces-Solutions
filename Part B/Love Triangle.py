n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
	a = arr[i]
	b = arr[a-1]
	c = arr[b-1]
	if c-1 == i and len(set([a,b,c])) == 3:
		print('YES')
		exit()
print('NO')