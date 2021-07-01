arr = []
max_cap = 0
cur = 0
n = int(input())
for i in range(n):
	a,b = map(int, input().split())
	cur += b-a
	max_cap = max(cur, max_cap)
print(max_cap)
