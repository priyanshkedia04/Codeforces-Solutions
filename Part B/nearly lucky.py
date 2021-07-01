def nearly_lucky(num):
	from collections import Counter
	d = dict(Counter(str(num)))
	four, seven = 0,0
	if '4' in d:
		four = d['4']
	if '7' in d:
		seven = d['7']
	n = four + seven
	d2 = dict(Counter(str(n)))
	four, seven = 0,0
	if '4' in d2:
		four = d2['4']
	if '7' in d2:
		seven = d2['7']
	if four + seven == len(str(n)):
		return True
	return False

n =  int(input())
print("YES" if nearly_lucky(n) else "NO")