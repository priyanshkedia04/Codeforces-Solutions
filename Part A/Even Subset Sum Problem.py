for i in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	even, odd1, odd2 = -1,-1,-1
	for j in range(n):
		if arr[j]%2 == 0:
			even = j
			break
		else:
			if odd1 == -1:
				odd1 = j
			else:
				odd2 = j
				break
	if even != -1:
		print(1)
		print(even + 1)
	elif odd1 != -1 and odd2 != -1:
		print(2)
		print(odd1 + 1, odd2 + 1)
	else:
		print(-1)