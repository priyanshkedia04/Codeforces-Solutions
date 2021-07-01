for _ in range(int(input())):
	n = int(input())
	arr = list(input())
	left = 0
	right = [0]*n

	if arr[-1] == '*':
		right[-1] = 1
	for i in range(n-2,-1,-1):
		if arr[i] == '*':
			right[i] = right[i+1] + 1
		else:
			right[i] = right[i+1]
	ans = 0
	for i in range(n):
		if arr[i] == '.':
			if right[i] < left:
				ans += right[i]
			else:
				ans += left
		else:
			left += 1
	print(ans)