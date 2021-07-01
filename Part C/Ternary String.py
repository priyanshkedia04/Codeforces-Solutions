for i in range(int(input())):
	s = input()
	arr = []
	temp = [s[0]]
	for i in s[1:]:
		if i == temp[-1]:
			temp.append(i)
		else:
			arr.append(temp)
			temp = [i]
	arr.append(temp)
	temp = []
	for i in range(1, len(arr)-1):
		if len(set([arr[i-1][0], arr[i][0], arr[i+1][0]])) == 3:
			temp.append(len(arr[i]) + 2)
	if len(temp) > 0:
		print(min(temp))
	else:
		print(0)

			