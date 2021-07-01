n,v = map(int, input().split())
tank = 1
cost = 0
for i in range(1, n+1):
	tank -= 1
	cost += min(n-i, v-tank) * i
	tank += min(n-i, v-tank)
	if tank >= n-i:
		break
print(cost)
