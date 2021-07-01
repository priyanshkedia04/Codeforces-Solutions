def presents():
	n = int(input())
	nums = list(map(int, input().split()))
	arr = [0]*len(nums)
	for i, pi in enumerate(nums):
		arr[pi-1] = i+1
	print(*arr)
presents()