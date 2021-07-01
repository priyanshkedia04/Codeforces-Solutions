def vanya_exams():
	from math import ceil
	n,r,avg = map(int, input().split())
	arr = []
	points = 0
	for i in range(n):
		a,b = map(int, input().split())
		points += a
		if a < r:
			arr.append([a,b])
	my_avg = points/n
	if my_avg >= avg:
		return 0
	points_required = int(ceil(n*avg - n*my_avg))
	count = 0
	arr.sort(key = lambda x: x[1])
	for i in range(len(arr)):
		temp = min(points_required, r-arr[i][0])
		count += temp*arr[i][1]
		points_required -= temp
		if points_required <= 0:
			return count
print(int(vanya_exams()))