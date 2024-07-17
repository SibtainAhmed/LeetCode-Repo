# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not to_delete: return [root]
        res = []
        delete = {i for i in to_delete}
        def dfs(node):
            if not node:
                return None
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val in delete:
                print(node.val)
                if l and l.val not in delete:
                    res.append(l)
                # else:
                #     print(node.val, 'None1')
                #     node.left = None
                if r and r.val not in delete:
                    res.append(r)
                # else:
                #     print(node.val, node.right, 'None2')
                #     node.right = None
                return None
                # node.val = None
            curr = TreeNode(node.val, l, r)
            return curr
        newRoot = TreeNode(to_delete[0], root)
        dfs(newRoot)
        # print(root)
        # res.append(root)
        return res
        
