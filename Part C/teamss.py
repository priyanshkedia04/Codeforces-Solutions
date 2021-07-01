n = int(input())
ans = 0
for i in range(n):
	arr = list(map(int, input().split()))
	ones = arr.count(1)
	if ones >= 2:
		ans += 1
print(ans)
