for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	for i in range(1, n+1):
		count = 0
		p_i = arr[i-1]
		while i != p_i:
			count += 1
			p_i = arr[p_i-1]
		print(count + 1, end = " ")