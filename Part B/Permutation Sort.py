for _ in range(int(input())):
	n = int(input())
	perm = list(map(int, input().split()))
	orig = list(range(1, n+1))
	if perm == orig:
		print(0)
	elif perm[0] == orig[0] or perm[-1] == orig[-1]:
		print(1)
	elif orig[0] == perm[-1] and orig[-1] == perm[0]:
		print(3)
	else:
		print(2)
