# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        queue.append(root)
        levelSum = []
        while queue:
            lSum = 0
            ln = len(queue)
            for _ in range(ln):
                node = queue.popleft()
                lSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelSum.append(lSum)
        if len(levelSum) < k:
            return -1
        else:
            levelSum.sort()
            return levelSum[len(levelSum)-k]