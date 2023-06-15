class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            firstWord = words[i]
            secondWord = words[i+1]
            j = 0
            while j < len(firstWord) and j < len(secondWord):
                if firstWord[j] != secondWord[j]:
                    if order_dict[firstWord[j]] > order_dict[secondWord[j]]:
                        return False
                    break
                j += 1

            if len(firstWord)-j and not(len(secondWord)-j):
                return False

        return True