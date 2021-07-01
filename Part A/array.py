def array(arr):
	set1 = []
	set2 = []
	set3 = []
	for i in arr:
		if i>0:
			set2.append(i)
		elif i == 0:
			set3.append(i)
		else:
			set1.append(i)
	if len(set1)%2 == 0:
		set3.append(set1.pop())
	if len(set2) == 0:
		set2.append(set1.pop())
		set2.append(set1.pop())
	print(len(set1), *set1)
	print(len(set2), *set2)
	print(len(set3), *set3)

input()
array(list(map(int, input().split())))