n = int(input())
arr = list(map(int, input().split()))
cost = arr[0]
energy = 0
for i in range(n-1):
	energy += arr[i] - arr[i+1]
	if energy < 0:
		cost += abs(energy)
		energy = 0
print(cost)