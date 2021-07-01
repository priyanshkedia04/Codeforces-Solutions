n = int(input())
arr = list(map(int, input().split()))
ans = 0
temp = 1
for i in range(1,n):
	if arr[i] != arr[i-1]:
		ans += temp*(temp+1)//2
		temp = 1
	else:
		temp += 1
print(ans+temp*(temp+1)//2)