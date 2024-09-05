class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        st, end = 0, len(nums)-1
        while st <= end:
            mid = (st+end)//2
            if nums[mid] == target:
                res[0] = mid
                end = mid-1
            elif nums[mid] > target:
                end = mid-1
            else:
                st = mid+1
        # print(res)
        st, end = 0, len(nums)-1
        while st <= end:
            mid = (st+end)//2
            if nums[mid] == target:
                res[1] = mid
                st = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                st = mid+1
        return res
        