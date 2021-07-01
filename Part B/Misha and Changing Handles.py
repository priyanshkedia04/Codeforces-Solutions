t = int(input())
d = {}
for i in range(t):
    old,new = input().split()
    d[new] = d.get(old,old)
    if old in d:
    	d.pop(old)
print(len(d))
for a,b in d.items():
    print(b,a)