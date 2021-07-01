n = int(input())
arr = list(map(int, input().split()))
ans = [0,0,0]
c = 0
for i in range(n):
	if c == 0:
		ans[c] += arr[i]
	elif c == 1:
		ans[c] += arr[i]
	else:
		ans[c] += arr[i]
		c = -1
	c += 1
p = ['chest', 'biceps', 'back']
print(p[ans.index(max(ans))])