n = int(input())
data = list(map(int, input().split()))
p = [0]*n
for i in range(n):
    p[data[i]-1] = data.index(data[i])+1
print(*p)
