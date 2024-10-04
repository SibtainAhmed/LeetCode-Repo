class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        st, end = 0, len(skill)-1
        skill.sort()
        fixSum = skill[st] + skill[end]
        while st<end:
            s,e = skill[st], skill[end]
            if s+e != fixSum:
                return -1
            res += s*e
            st += 1
            end -= 1
        return res