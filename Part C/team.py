def team(n,m):
	pm = int(m/2)
	rm = (m%2)
	if n+1 == pm:
		if rm == 0:
			ans = ["110"]*n
			ans.append("11")
			print("".join(ans))
		else:
			print(-1)
	elif pm+1 == n:
		ans = ["011"]*pm
		ans.append('0')
		if rm == 1:
			ans.append('1')
		print("".join(ans))
	elif n >= pm and n <= m:
		ans = ["110"]*(2*pm - n)
		ans.extend(["1010"]*(n-pm))
		if rm == 1:
			ans.append('1')
		print("".join(ans))
	elif n-1 == m:
		ans = ['01']*m
		ans.append('0')
		print("".join(ans))
	else:
		print(-1)

n, m = map(int, input().split())
team(n,m)