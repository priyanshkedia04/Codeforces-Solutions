arr = []
for i in range(1,10):
	arr.extend([str(i)*k for k in range(1, 5)])
for _ in range(int(input())):
	ans = 0
	for i in range(arr.index(input()) + 1):
		ans += len(arr[i])
	print(ans)
