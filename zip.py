# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = list(map(int, input().split()))
data = []
for _ in range(X):
    subject = list(map(float, input().split()))
    data.append(subject)
for i in zip(*data):
    print(sum(i)/X)