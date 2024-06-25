# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        sumVal = 0
        def dfs(node):
            if not(node):
                return 0
            nonlocal sumVal
            r = dfs(node.right)
            node.val = sumVal =  sumVal + node.val
            l = dfs(node.left)
            return node
        
        return dfs(root)
