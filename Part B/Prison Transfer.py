n,t,c = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
temp = []
for i in arr:
	if i <= t:
		temp.append(i)
	else:
		ans.append(temp[:])
		temp = []
if temp:
	ans.append(temp)

out = 0
for i in ans:
	if len(i) >= c:
		out += len(i) -c + 1
print(out)