def isprime(n):
	flag = True
	for j in range(2, int(n**0.5) + 1):
		if n%j == 0:
			flag = False
			break
	return flag

n, m = map(int, input().split())
for i in range(n+1, m):
	if isprime(i):
		print("NO")
		exit()
if isprime(m):
	print("YES")
else:
	print("NO")