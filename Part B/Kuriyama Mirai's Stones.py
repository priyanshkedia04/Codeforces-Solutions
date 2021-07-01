n = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
sort_arr = sorted(arr)
for i in range(1, n+1):
	arr[i] += arr[i-1]
	sort_arr[i] += sort_arr[i-1]
for i in range(int(input())):
	type,l,r = map(int, input().split())
	if type == 1:
		print(arr[r] - arr[l-1])
	else:
		print(sort_arr[r] - sort_arr[l-1])