def petrbook(n, arr):
	total = sum(arr)
	if n > total:
		r = n%total

		s = 0
		if r == 0:
			for i in range(len(arr)):
				s += arr[i]
				if s == total:
					return i+1

		s = 0
		for i in range(len(arr)):
			s += arr[i]
			if s >= r:
				return i+1
		
	elif total == n:
		s = 0
		for i in range(len(arr)):
			s += arr[i]
			if s == total:
				return i+1
		
	else:
		s = 0
		for i in range(len(arr)):
			s += arr[i]
			if s >= n:
				return i+1
n = int(input())
arr = list(map(int, input().split()))
print(petrbook(n, arr))
