primes = [True]*(2*(10**5) + 1)

for i in range(2,int((2*(10**5) + 1)**0.5 + 1)):
	if primes[i]:
		for j in range(2*i,len(primes),i):
			primes[j] = False
primes = [i for i in range(2,len(primes)) if primes[i]]
print(len(primes))
print(primes[-1])


def bin_serach(n):
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

print(bin_serach(5))
print(bin_serach(55))
print(bin_serach(100))
print(bin_serach(154))
print(bin_serach(123))
print(bin_serach(78))