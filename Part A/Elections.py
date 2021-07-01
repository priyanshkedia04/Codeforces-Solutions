n,m = map(int, input().split())
votes = [0]*n
for i in range(m):
	arr = list(map(int, input().split()))
	idx = arr.index(max(arr))
	votes[idx] += 1
print(votes.index(max(votes)) + 1)