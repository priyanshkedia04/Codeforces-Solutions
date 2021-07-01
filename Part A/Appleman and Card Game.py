n,k = map(int, input().split())
s = input()
from collections import Counter
arr = list(sorted(Counter(s).values(), reverse = True))
points = 0
idx = 0
while k > 0:
	temp = min(arr[idx], k)
	k -= temp
	points += temp*temp
	idx += 1
print(points)