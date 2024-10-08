class Solution:
    def minSwaps(self, s: str) -> int:
        op = close = res = 0
        for br in s:
            if br == '[':
                op += 1
            else:
                close += 1
            if close>op:
                res += 1
                op += 1
                close -= 1
               
                    # res += 1
        return res
            # if op > 1 or close>1:
            #     res += 1
            #     op -= 1
            #     close -= 1
        # return res
