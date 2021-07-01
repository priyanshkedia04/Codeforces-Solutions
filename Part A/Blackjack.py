n = int(input())
if n<= 10:
	print(0)
	exit()
remain = n-10
if 2<= remain < 10:
	print(4) 
elif remain == 10:
	print(15)
elif remain == 1 or remain == 11:
	print(4)
else:
	print(0)