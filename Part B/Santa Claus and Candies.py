n = int(input())
arr = []
i = 1
while n >= i:
	arr.append(i)
	n -= i
	i += 1
arr[-1] += n
print(len(arr))
print(*arr)


