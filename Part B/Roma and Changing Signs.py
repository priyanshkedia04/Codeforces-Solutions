n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(len(arr)):
	if k > 0 and arr[i] < 0:
		k -= 1
		arr[i] = abs(arr[i])
	else:
		break
if k>0 and k%2 == 1:
	print(sum(arr) - 2*min(arr))
else:
	print(sum(arr))