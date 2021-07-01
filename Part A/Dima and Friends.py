a=int(input())+1
b=sum(map(int,input().split()))
print(sum((b+i)%a!=1 for i in range(1,6)))