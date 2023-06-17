from collections import Counter
count = 0
for _ in range(int(input())):
    data_count = Counter(input())
    if data_count['1'] >= 2:
        count += 1
print(count)