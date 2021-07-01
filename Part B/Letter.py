from collections import Counter

s1 = dict(Counter(list(input())))
s2 = dict(Counter(list(input())))
count = 0

if ' ' in s2:
	del s2[' ']

for i in s2:
	if i in s1 and i:
		if s1[i] >= s2[i]:
			count += 1
if count == len(s2):
	print("YES")
else:
	print("NO")