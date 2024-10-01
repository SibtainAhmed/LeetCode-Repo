class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = defaultdict(int)
        for val in arr:
            rem[val%k]+=1
        # print(rem)
        for key in rem.keys():
            value = rem[key]
            if not(key):
                if value%2==0:continue
                else: return False
            if rem[key] == rem[abs(key-k)]:continue
            else: return False
        return True
