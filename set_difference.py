# Enter your code here. Read input from STDIN. Print output to STDOUT
englishCount = input()
englishSet = set(input().split())
frenchCount = input()
frenchSet = set(input().split())
print(len(englishSet-frenchSet))