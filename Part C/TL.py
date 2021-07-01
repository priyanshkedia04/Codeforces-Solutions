n,m = map(int, input().split())
right = list(map(int, input().split()))
wrong = list(map(int, input().split()))

ans = max(2*min(right), max(right))

if ans < min(wrong):
	print(ans)
else:
	print(-1)