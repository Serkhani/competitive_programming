for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    
    # i = 0
    # while i<len(b)-1:
    # # for i in range(len(ans)):
    #     ans[i] = b[i]
    #     r = b[len(b)-1-i]
    #     i+=1
    #     ans[i] = r
    #     i+=1
    #     # print(*ans)

    l, r = 0, len(b)-1
    idx = 0
    while l<r:
        ans[idx] = b[l]
        l+=1
        idx+=1
        ans[idx] = b[r]
        r-=1
        idx+=1
    if n%2:
        ans[idx] = b[l]


    # ans[idx] = b[l]
        # print(*ans)
    # for i in range(0,r,2):
    #     ans[l] = b[i]
        # ans[r] = b[i+1]
        # l+=1
        # r-=1
    print(*ans)