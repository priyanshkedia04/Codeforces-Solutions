n = int(input())
arr = list(map(int, input().split()))
ans = []
prev = arr[0]
temp = 1
m = 0
for i in arr[1:]:
	if i == prev:
		temp += 1
	else:
		ans.append(temp)
		temp = 1
		prev = i
ans.append(temp)
for i in range(len(ans) - 1):
	m = max(m, min(ans[i], ans[i+1]))

print(2*m)