for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	m = max(arr)
	flag = False
	for i in range(n):
		if arr[i] == m:
			if i+1<n:
				if arr[i] > arr[i+1]:
					flag = True
					print(i+1)
					break
			if i-1 >= 0:
				if arr[i] > arr[i-1]:
					flag = True
					print(i+1)
					break
	if flag is False:
		print(-1)