a = int(input())
b = int(input())
c = a+b
n_a, n_b, n_c = [],[],[]
for i in str(a):
	if i != '0':
		n_a.append(i)

for i in str(b):
	if i != '0':
		n_b.append(i)

for i in str(c):
	if i != '0':
		n_c.append(i)

n_c = int("".join(n_c))
n_a = int("".join(n_a))
n_b = int("".join(n_b))
 
if n_a + n_b == n_c:
	print("YES")
else:
	print("NO")