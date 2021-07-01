inp = []
for i in range(5):
	inp.append(int(input()))
k,l,m,n,d = inp
arr = list(range(1, d+1))
temp = arr[::k] + arr[::l]+ arr[::m] + arr[::n]
print(len(set(arr[k-1::k] + arr[l-1::l]+ arr[m-1::m] + arr[n-1::n])))