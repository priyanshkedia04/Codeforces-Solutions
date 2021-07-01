n,m = map(int, input().split())
plane = list(map(int, input().split()))
min_plane, max_plane = [], []
min_plane[:], max_plane[:] = plane, plane
max_plane = [-1*i for i in max_plane]
from heapq import heapify, heappop, heappush
heapify(min_plane)
heapify(max_plane)
ans_min = 0
ans_max = 0
for i in range(n):
	temp = heappop(min_plane)
	ans_min += temp
	if temp-1 != 0:
		heappush(min_plane, temp-1)

	temp = abs(heappop(max_plane))
	ans_max += temp
	if temp-1 != 0:
		heappush(max_plane, -1*(temp-1))
print(ans_max, ans_min)
