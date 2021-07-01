def bin_search(x):
	l = 0
	r = len(arr)-1
	while l <= r:
		m = (l+r) // 2
		if arr[m] == x:
			return m
		elif arr[m] > x:
			r = m-1
		else:
			l = m+1
	return r + 1
n,m = map(int, input().split())
rooms = list(map(int, input().split()))
letters = list(map(int, input().split()))
arr = [rooms[0]]
ans = []
for i in rooms[1:]:
	arr.append(arr[-1] + i)
for i in letters:
	d_idx = bin_search(i)
	room = rooms[d_idx] - (arr[d_idx] - i)
	ans.append([d_idx + 1, room])

for i in ans:
	print(*i)
