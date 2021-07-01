t=int(input())
for _ in range(t):
    n , q = map(int,input().split())
    s = input()
    for i in range(q):
        a , b = map(int,input().split())
        if s[a-1] in s[0:a-1] or s[b-1] in s[b:]:
            print("YES")
        else:
            print("NO")