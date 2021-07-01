n = int(input())
if n == 0:
	print(0,0,0)
	exit()
if n == 1:
	print(0,0,1)
	exit()
arr = [0,1]
while arr[-1] != n:
	arr.append(arr[-1] + arr[-2])

print(arr[-4], arr[-3], arr[-3])