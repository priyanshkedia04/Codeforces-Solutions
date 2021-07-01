def color_fence(v, arr):
	from collections import defaultdict
	d = defaultdict(list)
	for i in range(len(arr)):
		d[arr[i]].append(i+1)
	d = dict(d)
	print(d)


v = int(input())
arr = list(map(int, input().split()))
color_fence(v, arr)