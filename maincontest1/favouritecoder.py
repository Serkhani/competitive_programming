bestPerfCount = 0
n = int(input())
codersPerformances = list(map(int,input().split()))
checked = set([])
for i in range(1,n):
    if (codersPerformances[i] < min(codersPerformances[:i]) or codersPerformances[i] > max(codersPerformances[:i])) and codersPerformances[i] not in checked:
        bestPerfCount+=1
        checked.add(codersPerformances[i])
print(bestPerfCount)


# 5
# 100 50 200 150 200
