n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
count = 0
flag = True
while n>0:
	n-=arr[count]
	count += 1
	if count == len(arr) and n>0:
		flag = False
		break
	if n <= 0:
		break
if flag:
	print(count)
else:
	print(-1)