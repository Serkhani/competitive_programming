def check(inputList: list[int]):
    return inputList[0]<inputList[1] and inputList[0]<inputList[2] and inputList[2]<inputList[3] and inputList[1]<inputList[3]


for _ in range(int(input())):
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    _list = r1+r2
    if check(_list):
        print("YES") 
    else:
        for i in range(4):
            _list[0], _list[1], _list[2], _list[3] = _list[2], _list[0], _list[3], _list[1]
            # print(*_list)
            # print(f"list:{_list}\ns_list:{s_list}")
            if check(_list):
                print("YES") 
                break
        else:
            print("NO")


# Thought it has to be sorted