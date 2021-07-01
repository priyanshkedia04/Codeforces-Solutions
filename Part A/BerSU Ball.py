n = int(input())
boys = sorted(list(map(int, input().split())))
m = int(input())
girls = sorted(list(map(int, input().split())))
b,g = 0, 0
count = 0
while b<n and g<m:
	if abs(boys[b] - girls[g]) <= 1:
		count += 1
		b+=1
		g+=1
	else:
		if boys[b] > girls[g]:
			g+=1
		else:
			b+=1
print(count)
