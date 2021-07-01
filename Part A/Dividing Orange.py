n,k = map(int, input().split())
arr = list(map(int, input().split()))
oranges = list(range(1, n*k + 1))
child = {i:[] for i in range(1, k+1)}
for i in range(k):
	child[i+1].append(arr[i])
remain = list(set(oranges) - set(arr))
ptr = 0
for i in range(k):
	child[i+1].extend(remain[ptr:ptr+n-1])
	ptr += n-1
	print(*child[i+1])

