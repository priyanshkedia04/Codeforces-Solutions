n = int(input())
arr =list(map(int, input().split()))
each = sum(arr)//2
if each%100 != 0:
	print("NO")
else:
	dp = [[False]*(each+1) for i in range(len(arr)+1)]
	for i in range(len(arr)+1):
		dp[i][0] = True
	for i in range(1, len(arr)+1):
		for j in range(1, each+1):
			if arr[i-1] <= j:
				dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
			else:
				dp[i][j] = dp[i-1][j]
	if dp[len(arr)][each]:
		print("YES")
	else:
		print("NO")