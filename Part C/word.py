s = input()
l = 'abcdefghijklmnopqrstuvwxyz'
u = set('abcdefghijklmnopqrstuvwxyz'.upper())
l = set(l)
l_c = 0
u_c = 0
for i in s:
	if i in u:
		u_c += 1
	else:
		l_c += 1
if l_c >= u_c:
	print(s.lower())
else:
	print(s.upper())