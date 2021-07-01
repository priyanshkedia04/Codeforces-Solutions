n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
if sum(arr)%2 == 0:
	print(s)
else:
	for i in sorted(arr):
		if i%2 != 0:
			print(s-i)
			exit()