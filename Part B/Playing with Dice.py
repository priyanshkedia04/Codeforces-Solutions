a,b = map(int, input().split())
arr = [0,0,0]
for i in range(1,7):
	if abs(i-a) < abs(i-b):
		arr[0] += 1
	elif abs(i-a) > abs(i-b):
		arr[2] += 1
	else:
		arr[1] += 1
print(*arr)