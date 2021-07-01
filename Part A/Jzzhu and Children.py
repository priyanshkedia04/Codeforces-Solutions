n,m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for i in arr:
	if i%m == 0:
		ans.append(i//m)
	else:
		ans.append(i//m + 1)
ans = ans[::-1]
print(n - ans.index(max(ans)))
