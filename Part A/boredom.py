k, a, n, s = int(input()), 0, 0, {0: 1}
for c in input():
  n += int(c)
  a += s.get(n-k, 0)
  s[n] = 1+s.get(n, 0)
print(a)