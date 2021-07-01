n,m = map(int, input().split())
arr = list(map(int, input().split()))
increment = 0
for i in range(m):
	temp = list(map(int, input().split()))
	if temp[0] == 1:
		arr[temp[1]-1] = temp[2] - increment
	elif temp[0] == 3:
		print(arr[temp[1]-1] + increment)
	else:
		increment+=temp[1]