n,m = map(int, input().split())
ans = 0
for i in range(int(n**0.5)+1):
	for j in range(int(m**0.5)+1):
		if i**2 + j == n and j**2 + i == m:
			ans += 1
print(ans)
