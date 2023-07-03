t = int(input())
for _ in range(t):
    n = int(input())
    volumes = list(map(int, input().split()))
    for i in range(1,n):
        if volumes[i-1]<=volumes[i]:
            print("YES")
            break
    else: print("NO")
    # O(n) Time complexity
    # O(1)  Space Complexity


# Thought we had to sort
# Used bubble sort
# thought my first implementaiton was slower
# finally thought that it was questioning the complexity