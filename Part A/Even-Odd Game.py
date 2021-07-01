for i in range(int(input())):
	n = int(input())
	arr = sorted(list(map(int, input().split())))
	result = 0
	for i in range(n):
		a = arr.pop()
		if i%2 == 0:
			if a%2 == 0:
				result += a
		else:
			if a%2 != 0:
				result -= a
	if result > 0:
		print('Alice')
	elif result < 0:
		print('Bob')
	else:
		print('Tie')