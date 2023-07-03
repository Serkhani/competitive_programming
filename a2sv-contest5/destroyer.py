from collections import Counter
for _ in range(int(input())):
    n = int(input())
    inputData = list(map(int, input().split()))
    _max = max(inputData)
    counter = Counter(inputData)
    for i in range(1, _max+1):
        if counter[i]>counter[i-1]:
            print("NO")
            break
    else: print("YES")


#thought of it like a bubble sum problem
#thought they were all in the same line
#found that all we needed to count the values and make sure that 
    # for each number x
    # the count of x should be less than or equal to the value greater than it