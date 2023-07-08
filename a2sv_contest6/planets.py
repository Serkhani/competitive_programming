from collections import Counter
for _ in range(int(input())):
    n,c = list(map(int, input().split()))
    data =  list(map(int, input().split()))
    minimum = 0
    for v in Counter(data).values():
        minimum += v if v<c else c
    print(minimum)