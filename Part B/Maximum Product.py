for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    l=[a[0]*a[1]*a[n-1]*a[n-2]*a[n-3],a[0]*a[1]*a[2]*a[3]*a[n-1],a[n-5]*a[n-4]*a[n-1]*a[n-2]*a[n-3]]
    print(max(l))