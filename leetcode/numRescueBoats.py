class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i, j = 0, len(people)-1
        people.sort()
        boatCount = 0
        while i <= j:
            if limit >= people[i] + people[j]:
              i+=1
            boatCount += 1
            j-=1
        return boatCount