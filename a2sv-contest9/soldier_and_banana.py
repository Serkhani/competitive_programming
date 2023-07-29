k, n, w =  map(int, input().split())
_sum = (w*(w+1))/2
amount_dued =  _sum*k
borrowed = amount_dued - n
print(int(borrowed)) if  borrowed>0 else print(0)
    