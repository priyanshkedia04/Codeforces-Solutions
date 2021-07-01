n = int(input())
arr = list(map(int, input().split()))
if len(arr) < 2:
	print("YES")
else:
	from collections import Counter
	d = Counter(arr)
	if len(arr)%2 == 0:
		if d.most_common(1)[0][1] > len(arr)//2:
			print("NO")
		else:
			print("YES") 
	else:
		if d.most_common(1)[0][1] > len(arr)//2 + 1:
			print("NO")
		else:
			print("YES") 