f=open("input.txt",'r');g=open("output.txt",'w')
n,m=map(int,f.readline().split())
g.write(['BG'*m+'B'*(n-m),'GB'*n+'G'*(m-n)][n<m])