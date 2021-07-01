# longest common substring
for i in range(int(input())):
	a = input()
	b = input()
	n = len(a)
	m = len(b)
	dp = [[0]*(m+1) for _ in range(n+1)]
	for j in range(1,n+1):
		for k in range(1,m+1):
			if a[j-1] == b[k-1]:
				dp[j][k] = 1+dp[j-1][k-1]
			else:
				dp[j][k] = 0
	max_len = 0
	for j in range(0,n+1):
		for k in range(0,m+1):
			max_len = max(max_len, dp[j][k])
	print(n+m-2*max_len)