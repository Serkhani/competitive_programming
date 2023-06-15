class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        curr = 0
        for i in range(n, 1, -1):
            curr = (k + curr - 1) % i
            friends.pop(curr)
            print(friends)
        return friends.pop()