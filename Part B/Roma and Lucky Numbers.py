n,k = map(int, input().split())
arr = list(input().split())
ans = 0
for i in arr:
	if i.count('4') + i.count('7') <= k:
		ans += 1
print(ans)
