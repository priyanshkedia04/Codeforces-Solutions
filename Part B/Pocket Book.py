n, _ = map(int, input().split())
names = [input() for _ in range(n)]
 
cnt = 1
for chs in zip(*names):
	cnt *= len(set(chs))
 
print(cnt % 1000000007)