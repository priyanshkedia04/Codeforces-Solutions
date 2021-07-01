lower = dict(zip(list('qrbnp'), [9,5,3,3,1]))
upper = dict(zip(list('QRBNP'), [9,5,3,3,1]))
white = 0
black = 0
for i in range(8):
	for j in input():
		if j in lower:
			black += lower[j]
		elif j in upper:
			white += upper[j]
if black > white:
	print('Black')
elif black < white:
	print('White')
else:
	print('Draw')

