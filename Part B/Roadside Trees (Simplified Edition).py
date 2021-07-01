n = int(input())
h = int(input())
ans = h + n
prev = h
for i in range(n-1):
	h = int(input())
	if h >= prev:
		ans += h-prev + 1
	else:
		ans += prev-h + 1
	prev = h
print(ans)