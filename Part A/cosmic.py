n, m, k = map(int, input().split())
R = {str(i): i - 1 for i in range(n+1)}
C = {str(i): i - 1 for i in range(m+1)}
ans = []
l = [input().split() for i in range(n)]
for i in range(k):
    q, x, y = input().split()
    if q == 'c':
        C[x], C[y] = C[y], C[x]
    elif q == 'r':
        R[x], R[y] = R[y], R[x]
    else:
        ans.append(l[R[x]][C[y]])
print('\n'.join(ans))