
for _ in range(int(input())):
    r = int(input())-1
    data = list(map(int, input().split()))
    data.sort()
    l = 0
    runningSum = 0
    while l<=r:
        runningSum+= data[r]-data[l]
        l+=1
        r-=1
    # print(f"ans: {runningSum}")
    print(runningSum)



# [1 5 6 3 4]
# [1,3,4,5,6]
# 6-1 5-3