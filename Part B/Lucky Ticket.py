n = int(input())
s = input()
f, s = s[:n//2], s[n//2:]
ff, fs = f.count('4'), f.count('7')
sf, ss = s.count('4'), s.count('7')

if all([ff==sf, fs==ss, ff+fs == n//2, sf+ss == n//2]):
	print('YES')
else:
	print('NO')