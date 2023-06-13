for _ in range(int(input())):
    rec1 = set(map(int, input().split()))
    rec2 = set(map(int, input().split()))
    constDim = rec2.intersection(rec1)
    val = False
    if len(constDim) == 1:
        val = set([sum(rec1.union(rec2).difference(constDim))]) == constDim
    elif len(constDim) == 2:
        f, s = constDim
        val = (2*f == s) or (2*s == f)
    print("Yes") if val else print("No")