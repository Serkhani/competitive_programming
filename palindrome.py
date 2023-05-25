class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        div = 1
        while div *10 <= x: #using div*10 because we are trying to get the most significant value less than x
            div *= 10
        while x:
            right = x%10# getting the ones
            left = x//div#checking the extreme end
            if left != right:# if they aren't equal, then can conclude that it is not a palindrome
                return False
            x %= div #removing the extreme left
            x //= 10 # removing the ones position
            div /= 100 # reducing the extreme end's position... by 100 because both ones and extremes are removed
        return True