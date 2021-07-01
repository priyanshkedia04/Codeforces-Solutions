def build_perm(n, arr):
	base = list(range(1, n+1))
	count = 0
	for i in range(len(arr)):
		count += abs(arr[i] - base[i])
	print(count)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

build_perm(n, arr)