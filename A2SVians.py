n = int(input())
members = set(input().split())
badMembers = set(input().split())
excellent_count = 0
for member in members:
    if member not in badMembers:
        char_count = {}
        for char in member:
            char_count[char] = char_count.get(char, 0) + 1
        if len(set(char_count.values())) == 1:
            excellent_count += 1
print(excellent_count)
