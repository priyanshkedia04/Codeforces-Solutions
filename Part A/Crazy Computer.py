n,c = map(int, input().split())
arr = list(map(int, input().split()))
ans = 1
for i in range(n-1):
	if arr[i+1] - arr[i] <= c:
		ans += 1
	else:
		ans = 1
print(ans)