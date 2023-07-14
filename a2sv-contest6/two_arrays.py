for _ in range(int(input())):
    n= int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        if b[i]-a[i]>1 or a[i]>b[i]:
            print("NO")
            break
    else: print("YES")

    #  a==b or a+1 ==b
    #  a!=b and b-a>1
    #  a>b=> False

    # 2-4= -2
    # 2-3= -1