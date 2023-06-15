for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data_copy = data.copy()
    operations = []
    data.sort()
    for i in range(1,n):
        idx = data_copy.index(data[i])
        remainder = (data[i-1] -(data[i]%data[i-1]) )% data[i-1] 
        data[i] += remainder 
        if remainder:
            operations.append((idx+1, remainder))
        data_copy[idx] = -1
    print(len(operations))
    for i in sorted(operations, key= lambda x: x[0]):
        print(*i)

        # f,s = data[i-1:i+1]
        # if s%f:#if false
        #     target = minimum**(i+1)
        #     while target<s:
        #         target *= minimum
        #     temp = target
        #     while (target-data[i]) >data[i]:#> 10**18:
        #         operations.append((i+1, data[i]))
        #         data[i] += data[i]
        #     operations.append((i+1, target -data[i]))
        #     data[i]+= (temp-data[i])
        
    # operations.sort(key=lambda x: x[0])
    # print(len(operations))
    # for i in operations:
    #     print(*i)
    # print(f"data: {data}")

    # x = num2-(num2%num1)