n = int(input())
for i in range(n):
	a = int(input())
	sides = 360/(180-a)
	if sides%1 != 0:
		print("NO")
	else:
		print("YES")