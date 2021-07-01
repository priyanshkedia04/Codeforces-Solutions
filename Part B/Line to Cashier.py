n = int(input())
input()
print(min([sum(map(lambda x: int(x)*5 + 15, input().split())) for i in range(n)]))