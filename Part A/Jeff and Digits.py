n = int(input())
arr = list(map(int, input().split()))
fives = arr.count(5)
zeros = arr.count(0)
ans = (fives//9)*9
if zeros:
	print(int('5'*ans + '0'*zeros))
else:
	print(-)