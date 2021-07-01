arr = []
for cnt in range(1,10):
	for num in range(1,10):
		arr.append(int(str(num)*cnt))
import bisect
for _ in range(int(input())):
	n = int(input())
	print(bisect.bisect_right(arr, n))