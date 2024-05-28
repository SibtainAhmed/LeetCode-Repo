"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = dict()
        
        def dfs(nod):
            if nod.val in visited:
                return visited[node.val]
            lst = []
            newNode = Node(nod.val,lst)
            visited[nod.val] = newNode
            for neigh in nod.neighbors:
                if neigh.val not in visited:
                    lst.append(dfs(neigh))
                else:
                    lst.append(visited[neigh.val])
            return newNode
        return dfs(node)
        