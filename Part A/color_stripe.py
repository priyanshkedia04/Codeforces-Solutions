n, k = map(int, input().split()) 
p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[: k] + 'A'
p = {p[i] : p[i + 1] for i in range(k)}
if k == 2:
    t = input()
    u, v = 'AB' * (n // 2) + 'A' * (n % 2), 'BA' * (n // 2) + 'B' * (n % 2)
    x, y = sum(int(u[i] != t[i]) for i in range(n)), sum(int(v[i] != t[i]) for i in range(n))
    if x < y:
        print(x)
        print(u)
    else:
        print(y)
        print(v)    
else:
    t, s = list(input()), 0
    for i in range(1, n):
        if t[i] == t[i - 1]:
            t[i] = p[t[i]]
            if i + 1 < n and t[i] == t[i + 1]: t[i] = p[t[i]]
            s += 1
    print(s)
    print(''.join(t))