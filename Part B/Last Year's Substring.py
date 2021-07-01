def solve():
    n = int(input())
    num = input()
    for i in range(5):
        if num[:i] + num[n - 4 + i:] == "2020":
            print("YES")
            return
    print("NO")
 
for _ in range(int(input())):
    solve()