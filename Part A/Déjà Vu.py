for i in range(int(input())):
	s = input()
	temp1 = s + 'a'
	temp2 = 'a' + s
	if temp2 != temp2[::-1]:
		print('YES')
		print(temp2)
	elif temp1 != temp1[::-1]:
		print('YES')
		print(temp1)
	else:
		print('NO')