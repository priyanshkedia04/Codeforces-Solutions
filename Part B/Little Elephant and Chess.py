arr = []
for i in range(8):
	arr.append(input())

for i in range(8):
	if arr[i][0] == arr[i][-1]:
		print("NO")
		exit()
	for j in range(7):
		if arr[i][j] == arr[i][j+1]:
			print("NO")
			exit()
print("YES")