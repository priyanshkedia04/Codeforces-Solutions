n = int(input())
a = []
b = []
for i in range(n):
	x,y = map(int, input().split())
	a.append(x)
	b.append(y)
ans = 0
opened = set()
for i in range(n):
	for j in range(n):
		if a[i] == b[j] and i!=j:
			ans += 1
			break
print(len(a)-ans)