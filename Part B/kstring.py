def kstring(s, k):
	if len(s)%k != 0:
		return ""
	else:
		from collections import Counter
		d = dict(Counter(s))
		ans = []
		for letter in d:
			count = d[letter]
			if count%k == 0:
				ans.append(letter*(count//k))
			else:
				return ""
		ans = "".join(ans)
		ans = ans*k
		return ans

k = int(input())
s = input()
a = kstring(s, k)
if not a:
	print(-1)
else:
	print(a)