n = int(input())
d = {i:[] for i in range(1, n+1)}
for i in range(2, n+1):
	d[int(input())].append(i)
for i in d:
	if d[i]:
		temp = 0
		for j in d[i]:
			if len(d[j]) == 0:
				temp += 1
		if temp < 3:
			print("No")
			exit()
print("Yes")