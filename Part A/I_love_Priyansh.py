n = int(input())
arr = list(map(int, input().split()))

large = arr[0]
small = arr[0]
ans = 0

for i in range(1, n):
	if arr[i] > large:
		ans += 1
		large = arr[i]
	elif arr[i] < small:
		ans += 1
		small = arr[i]
	else:
		pass
print(ans)