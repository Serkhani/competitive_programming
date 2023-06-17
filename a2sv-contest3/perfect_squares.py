import math
n = int(input())
data = list(map(int, input().split()))
l_perfect_square = -math.inf
for i in data:
    if i<0:
        l_perfect_square = max(l_perfect_square, i)
        continue
    sqrt = math.sqrt(i)
    if not sqrt.is_integer():
        l_perfect_square = max(l_perfect_square, i)
print(l_perfect_square)