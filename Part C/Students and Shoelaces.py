n,m = map(int, input().split())
arr = []
for i in range(m):
	arr.append(list(map(int, input().split())))
s = set()
ans = 0
while True:
	count = [0]*(n)
	for a,b in arr:
		if a not in s and b not in s:
			count[a-1] += 1
			count[b-1] += 1
	flag = False
	for i in range(n):
		if count[i] == 1:
			flag = True
			s.add(i+1)
	if flag is False:
		print(ans)
		exit()
	ans += 1