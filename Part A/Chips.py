n,m = map(int, input().split())
arr = list(range(1, n+1))
s = sum(arr)
remain = m%s

for i in arr:
	if i <= remain:
		remain -= i
	else:
		break
print(remain)


