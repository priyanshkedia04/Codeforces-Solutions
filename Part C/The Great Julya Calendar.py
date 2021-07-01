n = int(input())
count = 0
while n>0:
	n-=max(map(int, str(n)))
	count += 1
print(count)