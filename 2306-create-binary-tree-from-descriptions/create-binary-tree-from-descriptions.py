# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, desc: List[List[int]]) -> Optional[TreeNode]:
        search = {}
        for p,c,d in desc:
            node = TreeNode(c)
            search[c] = node
        # return root
        root = None
        for p,c,d in desc:
            if p in search:
                continue
            else:
                root = p
                search[p] = TreeNode(p)
                break
        for p,c,l in desc:
            if l:
                search[p].left = search[c]
            else:
                search[p].right = search[c]
        return search[root]

