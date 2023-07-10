for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    maxIdx, minIdx = 0,0
    for i in range(len(data)):
        if data[i]>data[maxIdx]:
            maxIdx = i
        if data[i]<data[minIdx]:
            minIdx = i
    print(minIdx+1, maxIdx+1)