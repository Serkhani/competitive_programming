n, m = map(int, input().split())
nList = list(map(int, input().split()))
mList = list(map(int, input().split()))
merged = []
pt_n, pt_m = 0, 0
while pt_n < n and pt_m < m:
    if nList[pt_n]<mList[pt_m]:
        merged.append(nList[pt_n])
        pt_n += 1
    else:
        merged.append(mList[pt_m])
        pt_m += 1
merged.extend(nList[pt_n:])
merged.extend(mList[pt_m:])
print(*merged)