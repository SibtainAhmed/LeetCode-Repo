class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        print(nums)
        
        def findMin(i,val):
            left, right = i+1, len(nums)-1
            mid = 0
            while left <= right:
                mid = ((left+right)//2)
                if nums[mid]+val >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            return left 
        
        
        def findMax(i,val):
            left, right = i+1, len(nums)-1
            mid = 0
            while left <= right:
                mid = ((left+right)//2)
                if nums[mid]+val >= upper+1:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        for i in range(len(nums)-1):
            n = nums[i]
            if max(n*2,n+nums[i+1]) > upper: 
                break
            mn = findMin(i,n)
            # if not(mn): continue
            mx = findMax(i,n)
            print(n, mn, mx)
            res += (mx-mn+1)
        return res