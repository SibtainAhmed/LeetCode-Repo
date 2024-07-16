# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        res = ''

        def dfs(node, val):
            if not node:
                return ('', False)
            if node.val == val:
                return ('', True)
            else:
                l = dfs(node.left, val)
                r = dfs(node.right, val)
                if l[1]:
                    return ("L"+l[0], True)
                elif r[1]:
                    return ("R"+r[0], True)
                else:
                    return ('', False)
        f = dfs(root, startValue)[0]
        s = dfs(root, destValue)[0]
        # print(f,'==', s)
        # for i in range(len(s)):
        #     if s[i] != f[i]:
        #         return s
        if not(f and s): return 'U'*len(f)+s
        if f[0] != s[0]: return 'U'*len(f)+s
        i = 0 
        while i < (min(len(f), len(s))):
            if s[i] != f[i]:
                # ind = i
                break
            i += 1
        f = 'U'*(len(f[i:]))
        return f+s[i:]
            