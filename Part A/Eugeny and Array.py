I = lambda: map(int, input().split())
n, m = I()
arr = I()
one, m_one = 0,0
for i in arr:
	if i == -1:
		m_one+=1
	else:
		one += 1
arr = []
for i in range(m):
	l,r = I()
	temp = r-l+1
	if temp%2 == 0 and one >= temp//2 and m_one >= temp//2:
		arr.append(1)
	else:
		arr.append(0)
print(*arr)