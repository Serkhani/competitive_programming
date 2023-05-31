from collections import Counter

X = int(input())
shoesSize = Counter(input().split())
runningSum = 0
for _ in range(int(input())):
    size_price = input().split()
    if shoesSize.get(size_price[0], 0):
        shoesSize[size_price[0]] = shoesSize.get(size_price[0], 0) -1
        runningSum += int(size_price[1])
print(runningSum)