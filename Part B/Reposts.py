d={'polycarp':1}
for _ in range(int(input())):a,b,c=input().lower().split();d[a]=d[c]+1
print(max(d.values()))