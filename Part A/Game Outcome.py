n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))
row_sum = []
col_sum = []
for i in range(n):
	row_sum.append(sum(arr[i]))
for i in range(n):
	temp = 0
	for j in range(n):
		temp += arr[j][i]
	col_sum.append(temp)
ans = 0
for i in range(n):
	for j in range(n):
		if col_sum[i] > row_sum[j]:
			ans +=1
print(ans)