for i in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	if len(arr) == 1:
		print("First")
	else:
		count = 0
		for i in arr:
			if i == 1:
				count += 1
			else:
				break
		if count == len(arr):
			if count%2 != 0:
				print("First")
			else:
				print("Second")
		else:
			if count%2 == 0:
				print("First")
			else:
				print("Second")