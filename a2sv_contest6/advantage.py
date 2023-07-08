for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    first, second = 0,0
    for i in data:
        if i>first:
            second, first = first, i
        elif i>second:
            second = i
    output = []
    for i in range(len(data)):
        if data[i] != first:
            output.append(data[i]-first)
        else:
            output.append(data[i]-second)
    print(*output)

# used max, got tle
# tried to get the first and second max to reduce time complexity