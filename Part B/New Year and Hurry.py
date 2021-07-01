n, k = map(int, input().split())
time = 4*60  - k
if time <= 4:
	print(0)
	exit()
arr = [i*5 for i in range(1,n+1)]
count = 0
i = 0
while time-arr[i] >= 0:
	time -= arr[i]
	i += 1
	count += 1
	if i==n:
		break
print(count)