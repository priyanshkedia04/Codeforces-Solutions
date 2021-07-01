def cut_ribbon():
	n,a,b,c = map(int, input().split())
	cutting = [a,b,c]
	cutting.sort()
	dp = [float("-inf")] * (n + 1) 
	dp[0] = 0
	for cut in cutting:
		for length in range(n+1):
			if cut <= length:
				dp[length] = max(dp[length], 1+dp[length-cut])
	print(dp[n])


cut_ribbon()