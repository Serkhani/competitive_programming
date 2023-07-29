n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
boys.sort()
girls.sort()
bPtr, gPtr = 0, 0
count = 0
while bPtr<n and gPtr<m:
    if boys[bPtr] == girls[gPtr] or abs(boys[bPtr]-girls[gPtr]) == 1:
        count+=1
        bPtr +=1
        gPtr +=1
    else:
        if boys[bPtr]>girls[gPtr]:
            gPtr += 1
        elif boys[bPtr]<girls[gPtr]:
            bPtr +=1
print(count)