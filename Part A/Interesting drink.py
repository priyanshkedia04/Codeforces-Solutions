import bisect
input()
x=sorted(map(int,input().split()))
for i in range(int(input())):
	m=int(input())
	print(bisect.bisect_right(x,m))