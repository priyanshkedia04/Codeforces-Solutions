n,k = map(int, input().split())
arr = sorted(list(zip(range(n), (map(int, input().split())))), key = lambda x: x[1])
ans = []
i = 0
while k-arr[i][1] >=0:
	k-=arr[i][1]
	ans.append(arr[i][0]+1)
	i+=1
	if i == n:
		break
print(len(ans))
print(*ans)
