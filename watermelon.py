def isDividable(n: int)-> bool:
    return (not n%2) and n>2

if __name__ == '__main__':
    userInput = int(input())
    print("YES") if isDividable(userInput) else print("NO")