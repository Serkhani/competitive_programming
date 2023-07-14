class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i = 0
        j = len(skill) -1
        skill.sort()
        ans = 0
        target = skill[i] + skill[j] 
        while i < j:
          if target == skill[i] + skill[j]:
            ans += (skill[i] * skill[j])
          else:
            return -1
          i += 1
          j -= 1
        return ans