n = int(input())
arr = list(map(int, input().split()))
l,r = 0,n-1
for i in range(n-1):
	if arr[i+1] < arr[i]:
		l = i
		break
for i in range(l, n-1):
	if arr[i+1] > arr[i]:
		r = i
		break
if sorted(arr) == arr[:l] + arr[l:r+1][::-1] + arr[r+1:]:
	print('yes')
	print(l+1,r+1)
else:
	print('no')
