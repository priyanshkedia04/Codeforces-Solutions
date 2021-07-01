n = int(input())
arr = list(map(int, input().split()))

if n<=2:
	print(n)
else:	
	max_seg = 2
	curr = 2

	for i in range(2, len(arr)):
		if arr[i-2] + arr[i-1] == arr[i]:
			curr += 1
		else:
			max_seg = max(curr, max_seg)
			curr = 2
	max_seg = max(curr, max_seg)
	print(max_seg)