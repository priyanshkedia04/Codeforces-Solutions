input()
print(sum(min(abs(x-y), 10-abs(x-y)) for x, y in zip(map(int, input()), map(int, input()))))