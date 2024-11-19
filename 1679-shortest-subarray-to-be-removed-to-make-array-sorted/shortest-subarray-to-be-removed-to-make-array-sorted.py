class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        r = n-1
        while r-1>=0 and arr[r-1]<=arr[r]:
            r -= 1
        res = r
        l = 0
        while l<r and l+1<n :
            while r<n and arr[l]>arr[r]:
                r += 1
            res = min(res, r-(l+1))
            if arr[l]>arr[l+1]:
                break
            l+=1
        return res