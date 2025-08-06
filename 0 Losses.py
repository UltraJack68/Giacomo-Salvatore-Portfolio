"""You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order."""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = dict()
        answer = [[],[]]
        for index, player in enumerate(matches):
            if player[1] not in loser:
                loser[player[1]] = 1
            else:
                loser[player[1]] += 1
        for player in matches:
            if player[0] not in loser:
                loser[player[0]] = 0
        
        for key in loser:
            if loser[key] >= 2:
                continue
            elif loser[key] == 1:
                answer[1].append(key)
            elif loser[key] == 0:
                answer[0].append(key)
        
        for sublist in answer:
            sublist.sort()

        return answer

