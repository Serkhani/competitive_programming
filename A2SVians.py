from collections import Counter
n = int(input())
goodMembers = set(input().split()) - set(input().split())
excellent_count = 0
for member in goodMembers:
    char_count = Counter(member)
    if len(set(char_count.values())) == 1:
        excellent_count += 1
print(excellent_count)
