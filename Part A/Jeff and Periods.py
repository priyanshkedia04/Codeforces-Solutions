n = int(input())
elements = list(map(int, input().split()))
i, d = 0, {}
 
for j in elements:
    if j in d:
        d[j].append(i)
    else:
        d[j] = [i]
    i += 1
 
final = []
for x, v in d.items():
    if len(v) == 1:
        final.append((x, 0))
    else:
        s = set([v[i] - v[i - 1] for i in range(1, len(v))])
        if len(s) == 1:
            final.append((x, s.pop()))
 
print(len(final))
 
s = ''
for i, j in sorted(final):
    s += str(i) + ' ' + str(j) + '\n'
 
print(s)
