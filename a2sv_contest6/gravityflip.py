n = int(input())
data = list(map(int, input().split()))
data.sort()
print(*data)

#thought about subracting edges...
#realized they were just sorting