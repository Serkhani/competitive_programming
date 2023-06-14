class Solution:
    def countPrimes(self, n: int) -> int:
        """
        create a list: first and second are always False
        for each member that is prime, 
        make the multiples of the number in the list False,
        because they are not prime
        """
        if n <= 2:
            return 0        
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for i in range(2, n):
            if isPrime[i] and i**2 <= n:
                for j in range(i**2, n, i):
                    isPrime[j] = False
        
        return sum(isPrime)
        # O(n^2)