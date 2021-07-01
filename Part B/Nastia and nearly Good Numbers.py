for _ in range(int(input())):
	a,b = map(int, input().split())
	if a%b == 0:
		print('NO')
		continue
	if b == 2:
		print('YES')
		print(a, a*3, a + a*3)
		continue
	arr = []
	remain = []
	for i in range(2*b):
		arr.append(a*(i+1))
		remain.append(a*(i+1)%b)
	print(arr)
	print(remain)
	d_remain = {}
	for idx, ele in enumerate(remain):
		d_remain[ele] = idx
	
	possible = []
	for x in d_remain:
		if x !=0 and b-x in d_remain:
			if arr[d_remain[x]] != arr[d_remain[b-x]]:
				possible.append((arr[d_remain[x]], arr[d_remain[b-x]]))
	print(possible)
	if len(possible) >= 1:
		print('YES')
		print(possible[0][0], possible[0][1], possible[0][0] + possible[0][1])
		continue
	print('NO')
