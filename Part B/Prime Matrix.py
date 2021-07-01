primes = [True]*(2*(10**5) + 1)

for i in range(2,int((2*(10**5) + 1)**0.5 + 1)):
	if primes[i]:
		for j in range(2*i,len(primes),i):
			primes[j] = False

primes = [i for i in range(2,len(primes)) if primes[i]]

def bin_search(n):
	l = 0
	r = len(primes)
	while l <= r:
		mid = (l+r)//2
		if primes[mid] == n:
			return n
		elif primes[mid] < n:
			l = mid+1
		else:
			r = mid-1
	return primes[(l+r)//2 + 1]

n,m = map(int, input().split())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))

min_cost = float('inf')
#check for rows
for i in range(n):
	temp = 0
	for j in range(m):
		temp += abs(arr[i][j] - bin_search(arr[i][j]))
	min_cost = min(min_cost, temp)

#check for cols
for j in range(m):
	temp = 0
	for i in range(n):
		temp += abs(arr[i][j] - bin_search(arr[i][j]))
	min_cost = min(min_cost, temp)
print(min_cost)
