for _ in range(int(input())):
	n = int(input())
	if n == 1:
		print(1)
	elif n == 2:
		print(-1)
	else:
		arr = list(range(1,n**2 + 1, 2)) + list(range(2, n**2 + 1, 2))
		for i in range(0, n**2, n):
			print(*arr[i:i+n])


