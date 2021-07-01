n, d = map(int, input().split())
arr = list(map(int, list(input())))
arr = [d if i == 1 else 0 for i in arr]
jumps = [float('inf')]*n
jumps[0] = 0
for i in range(1, n):
	for j in range(0, i):
		if arr[j] + j >= i:
			jumps[i] = min(jumps[j] + 1 , jumps[i])
if jumps[-1] != float('inf'):
	print(jumps[i])
else:
	print(-1)