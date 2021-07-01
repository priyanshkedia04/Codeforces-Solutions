n = int(input())
arr = sorted(list(map(int, input().split())))
if n<=2:
	print(0)
	print(*arr)
	exit()
ans = [0]*n
ans[1::2] = arr[:n//2]
ans[0::2] = arr[n//2:]
print((n-1)//2)
print(*ans)
