for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    cnt=dict()
    for i in li:
        if i in cnt:
            cnt[i]+=1
        else:
            cnt[i]=1
    m=max(cnt, key= lambda x: cnt[x])
    m=cnt[m]
    if(m>n-m):
        print(2*m-n)
    else:
        if(n%2==0):
            print(0)
        else:
            print(1)