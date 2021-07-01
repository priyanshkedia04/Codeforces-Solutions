for i in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	s = set()
	for j in range(n):
		if arr[j] not in s:
			s.add(arr[j])
		else:
			if arr[j] + 1 not in s:
				s.add(arr[j] + 1)

	print(len(s))