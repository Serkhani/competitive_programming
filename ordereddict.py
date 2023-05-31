# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

invoice = OrderedDict()
for _ in range(int(input())):
    data = input().split()
    price = int(data.pop())
    name = " ".join(data)
    invoice[name] = invoice.get(name, 0) + price
for name, price in invoice.items():
    print(name, price)