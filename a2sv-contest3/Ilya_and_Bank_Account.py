balance = int(input())
if balance >= 0:
    print(balance)
else:
    balance *= -1
    ones = balance%10
    hundreds = (balance%100)//10
    balance //= 10
    balance += 0 if hundreds<ones else (ones-hundreds)  
    print(-balance)
