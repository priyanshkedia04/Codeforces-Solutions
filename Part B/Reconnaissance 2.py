n = int(input())
arr = list(map(int, input().split()))
m = float("inf")
idx = 0
for i in range(len(arr)-1):
	if abs(arr[i] - arr[i+1]) <= m:
		m = abs(arr[i] - arr[i+1])
		idx = i
if abs(arr[0] - arr[-1]) <= m:
	print(1,n)
else:
	print(idx+1, idx+2)