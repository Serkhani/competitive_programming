for _ in range(int(input())):
    r = int(input())-1
    s = input()
    l = 0
    while l<r:
        if (s[l]=='1' and s[r]=='0') or (s[l]=='0' and s[r]=='1'):
            l+=1
            r-=1
        else: break
    print(r-l+1)
