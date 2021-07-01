n = int(input())
ans = 0
while n > 9:
	n = sum(map(int, list(str(n))))
	ans += 1
print(ans)
