n = int(input())
odd, even = n//2, n//2
if n%2 != 0:
	odd += 1
print(even*(even+1) -odd**2)
