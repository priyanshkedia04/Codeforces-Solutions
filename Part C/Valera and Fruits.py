n,limit = map(int, input().split())
arr= [0]*(3000+1)
for i in range(n):
	a,b = map(int, input().split())
	arr[a]+=b
next = 0
fruits = 0
for i in range(1,3001):
	v = limit
	temp = min(v, next)
	fruits += temp
	v -= temp
	temp = min(v, arr[i])
	fruits += temp
	next = arr[i] - temp
v = limit
fruits += min(v, next)
print(fruits)