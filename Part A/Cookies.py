n = int(input())
arr = list(map(int, input().split()))
ans = 0
s = sum(arr)
for i in arr:
	if (s-i)%2 == 0:
		ans += 1
print(ans)