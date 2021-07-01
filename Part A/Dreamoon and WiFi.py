from itertools import product
sent = input()
revieved = input()
s = 0
r = [0,0,0]
for i in sent:
	if i == '+':
		s+=1
	else:
		s-=1
for i in revieved:
	if i == '+':
		r[0] += 1
	elif i == '-':
		r[1] += 1
	else:
		r[2] += 1
perms = [sum(i)+r[0]-r[1] for i in list(product([1,-1], repeat = r[2]))]
ans = perms.count(s)/len(perms)
print("%.9f" % ans)

