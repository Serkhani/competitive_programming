for i in range(int(input())):
    matrix = []
    n, m = map(int, input().split())
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    maxRunningSum = 0
    for i in range(n):
        for j in range(m):
            dx = 1
            runningSum = matrix[i][j]
            # primary diagonal
            while i+dx<n and j+dx<m:
                runningSum += matrix[i+dx][j+dx]
                dx+=1
            dx = 1
            while j-dx>=0 and i-dx>=0:
                runningSum += matrix[i-dx][j-dx]
                dx += 1
            # secondary diagonal
            dx = 1
            while i+dx<n and j-dx>=0:
                runningSum += matrix[i+dx][j-dx]
                dx += 1
            
            dx = 1
            while i-dx>=0 and j+dx<m:
                runningSum += matrix[i-dx][j+dx]
                dx += 1
            maxRunningSum = max(runningSum, maxRunningSum)
    print(maxRunningSum)
            


# n = 5
# for i in range(n):
#     print(n-1-i)