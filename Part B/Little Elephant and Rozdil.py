n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
if len(arr)>1:
	if sorted_arr[0] == sorted_arr[1]:
		print("Still Rozdil")
	else:
		print(arr.index(sorted_arr[0]) + 1)
else:
	print(arr.index(sorted_arr[0]) + 1)