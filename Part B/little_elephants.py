n = input()
arr = []
flag = False
for i in n:
	if i != '0':
		arr.append(i)
	else:
		if flag:
			arr.append(i)
		else:
			flag = True
if len(arr) == len(n):
	arr.pop()
print("".join(arr))