n1 = input()
n2 = input()
arr = []
for i in range(len(n1)):
	if n1[i] == n2[i]:
		arr.append('0')
	else:
		arr.append('1')
print("".join(arr))