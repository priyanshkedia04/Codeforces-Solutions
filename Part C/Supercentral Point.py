n = int(input())
a = [list(int(a) for a in input().split()) for i in range(n)]
count=0
for x,y in a:
     q=w=e=r=0
     for x1,y1 in a:
          if x==x1 and y<y1:q=1
          if x==x1 and y>y1:w=1
          if x<x1 and y==y1:r=1
          if x>x1 and y==y1:e=1
     if q==w==e==r==1:count+=1
print(count)