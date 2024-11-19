class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # print(nums[2594:2701],'\n')
        res = i = sm = 0
        visited = set()
        # index = {}
        while i<len(nums):
            n = nums[i]
            if n in visited:
                for j in range(max(0,i-len(visited)), i):
                    # if nums[j] not in visited: continue
                    visited.remove(nums[j])
                    sm -= nums[j]
                    if nums[j] == n:
                        break
            visited.add(n)
            # index[n] = i
            sm += n
            if len(visited) == k:
                res = max(res, sm)
                sm -= nums[(i+1)-k]
                # if nums[(i+1)-k] == 9089:
                #     print(f'i={i}, (i+1)-k={(i+1)-k}, nums[(i+1)-k] = {nums[(i+1)-k]}')
                #     print(visited)
                visited.remove(nums[(i+1)-k])
            i += 1
        return res