for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = [0] * n
    new_arr[0], new_arr[-1] = arr[0], arr[-1]
    for i in range(1,n-1):
        new_arr[i] = min(arr[i], arr[i-1])
    print(*new_arr)