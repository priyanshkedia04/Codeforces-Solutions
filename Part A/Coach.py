n,m = map(int, input().split())
d = {i:[] for i in range(1, n//3 + 1)}
idx = [-1 for i in range(n+1)]
arr = []
key = 1
for i in range(m):
	a,b = map(int, input().split())
	if idx[a] == idx[b] and idx[a] != -1:
		continue
	elif idx[a] == -1 and idx[b] == -1:
		idx[a] = key
		idx[b] = key
		if key > n//3:
			print(-1)
			exit()
		d[key].append(a)
		d[key].append(b)
		key += 1
	elif idx[a] != -1 and idx[b] == -1:
		idx[b] = idx[a]
		if len(d[idx[a]]) < 3:
			d[idx[a]].append(b)
		else:
			print(-1)
			exit()
	elif idx[a] == -1 and idx[b] != -1:
		idx[a] = idx[b]
		if len(d[idx[b]]) < 3:
			d[idx[b]].append(a)
		else:
			print(-1)
			exit()
	else:
		print(-1)
		exit()
remain = []
for i in range(1,n+1):
	if idx[i] == -1:
		remain.append(i)
ptr = 0
for i in d:
	if len(d[i]) < 3:
		for j in range(3-len(d[i])):
			d[i].append(remain[ptr])
			ptr += 1
	print(*d[i])
