# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n):
    userInput = input()
    d[userInput] = d.get(userInput, 0) + 1
print(len(d))
for i in d.values():
    print(i, end=' ')