n,s = map(int, input().split())
arr = []
for i in range(n):
	a,b = map(int, input().split())
	arr.append([a,b])
arr.sort(reverse  = True)
elapsed = 0
for i in range(n):
	elapsed += s-arr[i][0]
	s = arr[i][0]
	elapsed += max(0, arr[i][1] - elapsed)
print(elapsed + s)

