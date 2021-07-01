import math
 
t = int(input())
 
for _ in range(t):
	n = int(input())
 
	C = [int(x) for x in input().split()]
 
	val = 0
 
	D = []
 
	for l in C[::-1]:
		val = max(val, l)
 
		if val == 0:
			D.append(0)
		else:
			D.append(1)
 
		val = val -1
 
 
	print(*D[::-1])