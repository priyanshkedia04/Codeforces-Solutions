n = int(input())
arr = list(map(int, input().split()))
zeros = 0
minus_one = 0
cost = 0
for i in arr:
	if i >= 1:
		cost += i-1
	elif i == 0:
		cost += 1
		zeros += 1
	elif i <= -1:
		minus_one += 1
		cost += abs(i+1)

if minus_one % 2 == 0:
	print(cost)
else:
	if zeros > 0:
		print(cost)
	else:
		print(cost + 2)



