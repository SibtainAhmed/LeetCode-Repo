class Solution:
    def countWinningSequences(self, s: str) -> int:
        
        moves = "FWE"
        n = len(s)

        def updateScore(alice,bob):
            if alice == bob:
                return 0
            elif hm[bob] == alice:
                return -1
            else:
                return 1
        
        hm = {
            "F": "W",
            "E": "F",
            "W": "E"
        }
        
        @lru_cache(None)
        def dp(i, score, prev):
            if i == n:
                return score > 0
            count = 0
            for move in moves:
                if move == prev: continue
                count += int(dp(i+1, score + updateScore(s[i],move), move))
            
            return count%1_000_000_007
        
        return dp(0, 0, "")
                
            
        