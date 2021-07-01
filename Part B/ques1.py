for _ in range(int(input())):
	n = int(input())
	s = input()
	d = {}
	flag = True
	for i in range(n):
		if s[i] not in d:
			d[s[i]] = i
		else:
			if d[s[i]] + 1 != i:
				flag = False
				break
			else:
				d[s[i]] = i
	if flag:
		print("YES")
	else:
		print("NO")
