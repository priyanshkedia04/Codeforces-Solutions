n = int(input())
ans = 0
prev = input()
for i in range(n-1):
	s = input()
	if prev != s:
		ans += 1
	prev = s
print(ans+1)
