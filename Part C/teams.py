def teams(k,array):
    array_2=[]
    for i in range(len(array)):
        if array[i]+k<=5:
            array_2.append(array[i]+k)
    teams=len(array_2)//3
    print(teams)
n,k=input().split()
array=[int(x) for x in input().split()]
teams(int(k),array)