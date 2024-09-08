# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        lst = []

        def dfsAdd(node):
            if not(node):
                return None
            if node.val == head.val: lst.append(node)
            dfsAdd(node.left)
            dfsAdd(node.right)
        dfsAdd(root)

        def dfs(tNode, lNode):
            if not(lNode):
                return True
            elif not(tNode): return False
            elif lNode.val == tNode.val:
                return dfs(tNode.left, lNode.next) or dfs(tNode.right, lNode.next)
            else:
                return False
        res = False
        for l in lst:
            res |= dfs(l,head)
        return res