n = int(input())
denoms = [100,20,10,5,1]
ans = 0
for coin in denoms:
	ans += n//coin
	n = n%coin
print(ans)