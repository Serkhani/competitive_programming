# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = list(map(int, input().split()))
d = defaultdict(list)
for i in range(1,n+1):
    d[input()].append(str(i))
    
for i in range(m):
    listdata = d[input()]
    if not listdata:
        print('-1')
    else:
        print(' '.join(listdata))