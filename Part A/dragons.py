def dragons(arr, s):
	while arr:
		if arr[-1][0] < s:
			s += arr[-1][1]
			arr.pop()
		else:
			return False
	if len(arr)>0:
		return False
	return True


arr = []
s, n = list(map(int, input().split()))
for i in range(n):
	x, y = list(map(int, input().split()))
	arr.append((x, y))
	arr.sort()
	arr = arr[::-1]
print("YES" if dragons(arr,s) else "NO")