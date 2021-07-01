def sereja_suffix(arr, l, n, m):
	dp = [0]*n
	dp[-1] = 1
	s = set()
	s.add(arr[-1])
	for i in range(n-2, -1, -1):
		dp[i] += dp[i+1]
		if arr[i] not in s:
			s.add(arr[i])
			dp[i] += 1
	for i in l:
		print(dp[i-1])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
l = []
for i in range(m):
	l.append(int(input()))

sereja_suffix(arr, l, n, m)