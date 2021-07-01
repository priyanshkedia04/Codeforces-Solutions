arr = []
for i in range(3):
	arr.append(list(map(int, input().split())))
max_sum = 0
s = 0	
for i in range(3):
	max_sum = max(max_sum, sum(arr[i]))
for i in range(3):
	arr[i][i] = max_sum - sum(arr[i])
	s += arr[i][i]
temp = (max_sum-s)//2
for i in range(3):
	arr[i][i] += temp
	print(*arr[i])