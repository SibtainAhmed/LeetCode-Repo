class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left

class NumArray:

    def __init__(self, nums: List[int]):
        diff = (2**(math.ceil(math.log2(len(nums)))))-len(nums)
        self.nums = nums + [0]*diff

        def buildTree(s,e):
            if e-s+1 <= 2:
                return TreeNode(self.nums[s]+self.nums[e])
            else:
                mid = (s+e)//2
                l = buildTree(s,mid)
                r = buildTree(mid+1,e)
                return TreeNode(l.val+r.val,l,r)
        # print(self.nums)
        self.root = buildTree(0,len(self.nums)-1)


    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        def propagate(node,s,e):
            node.val += diff
            if e-s+1 <= 2:
                return
            else:
                mid = (s+e)//2
                if s <= index <= mid:
                    return propagate(node.left,s,mid)
                return propagate(node.right,mid+1,e)
        propagate(self.root,0,len(self.nums)-1)
        # print(self.nums)

    def sumRange(self, left: int, right: int) -> int:
        
        def findSum(node,s,e):
            if s == e: return self.nums[s]
            elif left<=s and e<=right:return node.val
            else:
                mid = (s+e)//2
                val = 0
                if mid>=left and s<=right:
                    val += findSum(node.left,s,mid)
                if e>=left and mid+1 <= right:
                    val += findSum(node.right,mid+1,e)
                return val
        return findSum(self.root,0,len(self.nums)-1)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)