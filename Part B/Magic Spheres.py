a,b,c = map(int, input().split())
x,y,z = map(int, input().split())
pos = 0
neg = 0
for i in [a-x,b-y,c-z]:
	if i > 0:
		pos += i//2
	else:
		neg += abs(i)
if pos>=neg:
	print('Yes')
else:
	print('No')

