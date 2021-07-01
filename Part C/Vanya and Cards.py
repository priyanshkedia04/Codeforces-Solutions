n,x = map(int, input().split())
arr = list(map(int, input().split()))
s = abs(sum(arr))
if s%x == 0:
	print(s//x)
else:
	print(s//x + 1)