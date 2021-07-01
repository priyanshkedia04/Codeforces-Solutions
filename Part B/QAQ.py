import itertools
s = input()
print(sum(map(lambda x: (x == ('Q', 'A', 'Q')), itertools.combinations(s, 3))))