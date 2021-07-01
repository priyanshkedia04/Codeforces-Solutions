arr=[1]*10
 
k=int(input())
x=1
i=0
while x<k:
	a=arr[i]
	x//=a
	arr[i]+=1
	x*=arr[i]
	i=(i+1)%10
 
s='codeforces'
ans=""
 
for i in range(10):
	ans+=s[i]*arr[i]
 
 
print(ans)
 