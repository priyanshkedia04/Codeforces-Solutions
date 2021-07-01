def dec_premutations(k, n):
	arr = list(range(1, n+1))
	temp = []
	for i in range(k):
		temp.append(arr[-(i+1)])
	temp.extend(arr[:len(arr)-k])
	print(*temp)

n,k = map(int, input().split())
dec_premutations(k,n)