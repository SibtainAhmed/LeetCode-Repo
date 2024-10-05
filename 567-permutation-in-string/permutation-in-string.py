class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):return False
        start = 0
        end = len(s1)
        s1Freq = Counter(s1)
        while end <= len(s2) and s1:
            if (s1Freq == Counter(s2[start:end])): return True
            start += 1
            end += 1
        return False