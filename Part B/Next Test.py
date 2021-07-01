n = int(input())
arr = list(map(int, input().split()))
print(sorted(set(range(1, max(arr)+2)) - set(arr))[0])