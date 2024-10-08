class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap)>=self.k:
            if self.heap:
                curr = heapq.heappop(self.heap)
            else: curr = -math.inf
            val = max(val, curr)
        heapq.heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)