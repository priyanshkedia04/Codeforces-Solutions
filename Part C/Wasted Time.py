n,k = map(int, input().split())
distance = 0
x, y = map(int, input().split())
for i in range(n-1):
	a,b = map(int, input().split())
	distance += ((x-a)**2 + (y-b)**2)**0.5
	x,y = a,b
total = k*distance
print('%.9f' %(total/50))