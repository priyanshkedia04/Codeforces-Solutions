for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    one = a.count(1)
    two = a.count(2)
    print('NO' if one % 2 or (two % 2 and one < 2) else 'YES')
