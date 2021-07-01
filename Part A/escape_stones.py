s = input()
l = []
r = []
for i in range(len(s)):
	if s[i] == 'l':
		l.append(i+1)
	else:
		r.append(i+1)
r.extend(l[::-1])
for i in r:
	print(i)