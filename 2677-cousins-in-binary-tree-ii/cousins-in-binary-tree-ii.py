# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append([root, 0])
        prevSum = 0
        while queue:
            currSum = 0
            ln = len(queue)
            for _ in range(ln):
                node, parentSum = queue.popleft()
                value = prevSum-parentSum
                node.val = value
                pSum = node.left.val if node.left else 0
                pSum += node.right.val if node.right else 0
                currSum += pSum
                if node.left:
                    queue.append([node.left,pSum])
                if node.right:
                    queue.append([node.right,pSum])
            prevSum = currSum
            # print(prevSum)
        return root