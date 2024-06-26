# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            nonlocal tree
            tree.append(node.val)
            inOrder(node.right)
        inOrder(root)
        print(tree)
        def arrayToBST(st, end):
            if st>end:
                return None
            mid = (st + end)//2
            root = TreeNode(tree[mid])
            root.left = arrayToBST(st,mid-1)
            root.right = arrayToBST(mid+1,end)
            return root
        return arrayToBST(0, len(tree)-1)