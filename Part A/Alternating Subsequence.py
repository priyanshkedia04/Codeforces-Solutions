for i in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	subseq = []
	temp = [arr[0]]
	for i in arr[1:]:
		if temp[-1] > 0 and i > 0:
			temp.append(i)
		elif temp[-1] < 0 and i < 0:
			temp.append(i)
		else:
			subseq.append(max(temp))
			temp = []
			temp.append(i)
	subseq.append(max(temp))
	print(sum(subseq))