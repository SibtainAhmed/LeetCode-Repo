class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:return False
        count = Counter(s)
        oddC = 0
        for v in count.values():
            if v%2:
                oddC += 1
        return True if oddC<=k else False