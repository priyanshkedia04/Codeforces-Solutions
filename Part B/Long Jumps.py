for i in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	jumps = [0]*n
	for i in range(n-1,-1,-1):
		if arr[i] + i > n-1:
			jumps[i] = arr[i]
		else:
			jumps[i] = arr[i] + jumps[arr[i] + i]
	print(max(jumps))
