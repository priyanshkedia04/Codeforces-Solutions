a,b = map(int, input().split())
arr = [b]
while b >= a:
	if b == a:
		print('YES')
		print(len(arr))
		print(*arr[::-1])
		exit()
	if b%2 == 0:
		b/=2
		arr.append(int(b))
	elif b%10 == 1:
		b = b//10
		arr.append(int(b))
	else:
		print('NO')
		exit()
print('NO')