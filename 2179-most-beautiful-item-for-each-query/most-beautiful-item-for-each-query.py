class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[0])
        maxBeauty, lastPrice = 1, -1
        newItems = []
        for i in range(len(items)):
            maxBeauty = max(maxBeauty, items[i][1])
            if items[i][0] == lastPrice:
                newItems[-1][1] = maxBeauty
                continue
            lastPrice = items[i][0]
            newItems.append([lastPrice, maxBeauty])
        def binarySearch(val):
            left, right = 0, len(newItems)-1
            mid = 1
            while left<right:
                mid = ((left+right)//2)+1
                if val >= newItems[mid][0]:
                    left = mid
                else:
                    right = mid - 1
            return newItems[right][1] if (mid>0 and val>=newItems[right][0]) else 0
        ans = []
        for q in queries:
            ans.append(binarySearch(q))
        return ans