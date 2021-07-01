k = int(input())
num = 19
while k>0:
	if sum(map(int,str(num)))==10:
		k-=1
	if k == 0:
		print(num)
		exit()
	num += 9
