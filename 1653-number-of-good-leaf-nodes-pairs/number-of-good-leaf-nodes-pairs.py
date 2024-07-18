# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        resVar = 0

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            res = []
            for l in left:
                for r in right:
                    if l+r<=distance:
                        nonlocal resVar
                        resVar += 1
                #     if r <= distance:
                #         res.append(r)
                # if l <= distance:
                #     res.append(l)
            res = left + right
            res = [val+1 for val in res]
            return res
        dfs(root)
        return resVar