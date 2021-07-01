n = int(input())
arr = list(map(int, input().split()))
max_length = 1
cur_len = 1
prev = arr[0]
for i in range(1,len(arr)):
	if arr[i] >= prev:
		cur_len += 1
		prev = arr[i]
	else:
		max_length = max(max_length, cur_len)
		cur_len = 1
		prev = arr[i]
max_length = max(max_length, cur_len)
print(max_length)