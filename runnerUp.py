if __name__ == '__main__':  
    n = int(input())
    arr = list(map(int, input().split()))
    winner, runnerUP = arr[0], arr[0]
    for i in range(1,n):
        if arr[i]>winner and arr[i] != winner:
            runnerUP = winner
            winner = arr[i]
        elif (arr[i]<winner and arr[i] >runnerUP) or (arr[i]<runnerUP and runnerUP == winner):
            runnerUP = arr[i]
        
    print(runnerUP)