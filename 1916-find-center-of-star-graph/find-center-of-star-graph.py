class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        check = {edges[0][0], edges[0][1]}
        return edges[1][0] if edges[1][0] in check else edges[1][1]
