n,t = map(int, input().split())
seq = list(input())

temp = [0 for i in range(n)]
temp[0] = seq[0]

for i in range(t):
	for j in range(1,len(seq)):
		if seq[j-1] == 'B' and seq[j] == 'G':
			temp[j-1] = 'G'
			temp[j] = 'B'
		else:
			temp[j] = seq[j]
	seq = temp[:]

print("".join(seq))
