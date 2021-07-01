def  function():	
	a = list(input())
	b = list(input())
	ans = []
	if len(a)!=len(b):
		print("NO")
		exit()
	for i in range(len(a)):
		if a[i] != b[i]:
			ans.append(i)
	if len(ans) == 0:
		print("YES")

	elif len(ans) == 2:
		b[ans[0]], b[ans[1]] = b[ans[1]], b[ans[0]]
		if a == b:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")

if a = b:
	print("YES")

return

