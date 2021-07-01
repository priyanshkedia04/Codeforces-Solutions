r, c = map(int, input().split())
a = [input() for _ in range(r)]
 
for i in range(r):
	if 'WS' in a[i] or 'SW' in a[i]:
		print('No')
		exit()
	if i != r - 1:
		for j in range(c):
			if a[i][j] + a[i+1][j] in ['WS', 'SW']:
				print('No')
				exit()
print('Yes')
for i in range(r):
    print(''.join(a[i].replace('.', 'D')))