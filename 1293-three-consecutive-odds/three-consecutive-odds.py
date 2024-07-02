class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i]%2:
                if sum(arr[i:i+3])%2:
                    return True
        return False