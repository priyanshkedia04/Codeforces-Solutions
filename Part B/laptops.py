n = int(input())
arr = []
for i in range(n):
	a,b = map(int, input().split())
	arr.append([a,b])
arr.sort()
print(arr)
flag = False
for i in range(n-1):
	if arr[i][1] > arr[i+1][1]:
		print("Happy Alex")
		print(arr[i][1], arr[i+1][1])
		flag = True
		break
if not flag:
	print('Poor Alex')