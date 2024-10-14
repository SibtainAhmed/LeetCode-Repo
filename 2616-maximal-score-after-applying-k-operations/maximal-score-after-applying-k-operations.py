class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            val = -heapq.heappop(nums)
            res += val
            heapq.heappush(nums, -math.ceil(val/3))
        return res