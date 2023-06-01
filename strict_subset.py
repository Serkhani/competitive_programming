# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split())
for _ in range(int(input())):
    issubSet = set(input().split())
    if not(setA.intersection(issubSet) == issubSet and setA.difference(issubSet)):
        print("False")
        break
else:print("True")