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
# # balance_str = input()
# balance = int(input())
# if balance >= 0:
#     print(balance)
# else:
#     # if len(balance_str) == 1: print("0")
#     # maxbal = -math.inf
#     # i = 1
#     # while i<len(balance_str):
#     #     if balance_str[i] != '0':
#     #         data = balance_str[:i] + balance_str[i+1:]
#     #         print(data)
#     #         maxbal = max(abs(int(data)),maxbal)
#     #     i+=1
#     # print(-maxbal)
#     # if balance>-10:
#     #     print("0")
#     # else:
#         balance *= -1
#         ones = balance%10
#         hundreds = (balance%100)//10
#         balance //= 10
#         balance += 0 if hundreds<ones else (ones-hundreds)
            

#         print(-balance)
        

# # thught it was supposed to be any digit
# # tried to use string
