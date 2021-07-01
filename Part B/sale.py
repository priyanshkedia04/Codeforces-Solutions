n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
print(abs(sum([i for i in arr if i < 0][:m])))