from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)
        for outcome in matches:
            winners[outcome[0]] = winners[outcome[0]] + 1
            losers[outcome[1]] = losers[outcome[1]] + 1
        winners_list, losers_list = [], []
        for winner in winners.keys():
            if not losers[winner]:
                winners_list.append(winner)
        for loser in losers.keys():
            if losers[loser] == 1:
                losers_list.append(loser)
        winners_list.sort()
        losers_list.sort()
        return [winners_list, losers_list]
