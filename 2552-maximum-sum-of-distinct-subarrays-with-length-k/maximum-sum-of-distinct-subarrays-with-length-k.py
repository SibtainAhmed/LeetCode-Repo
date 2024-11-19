class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = i = sm = 0
        visited = set()
        while i<len(nums):
            n = nums[i]
            if n in visited:
                for j in range(max(0,i-len(visited)), i):
                    visited.remove(nums[j])
                    sm -= nums[j]
                    if nums[j] == n:
                        break
            visited.add(n)
            sm += n
            if len(visited) == k:
                res = max(res, sm)
                sm -= nums[(i+1)-k]
                visited.remove(nums[(i+1)-k])
            i += 1
        return res