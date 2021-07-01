n = int(input())
arr = []
for i in range(n):
	a,b = map(int, input().split())
	arr.append([a,b])
arr.sort(reverse = True, key = lambda x: x[0])
arr.sort(reverse = True, key = lambda x: x[1])
points = arr[0][0]
cards = arr[0][1]
i = 1
while cards > 0 and i < len(arr):
	points += arr[i][0]
	cards += arr[i][1]
	cards -= 1
	i+=1
print(points)