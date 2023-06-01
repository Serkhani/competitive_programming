# Enter your code here. Read input from STDIN. Print output to STDOUT
elementNum = int(input())
data = tuple(map(int, input().split()))
print(data)
print(hash(data))