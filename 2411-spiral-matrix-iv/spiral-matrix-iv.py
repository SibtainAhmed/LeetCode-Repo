# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        r = 0
        c = -1
        direct = 1
        while head:
            m -= 1
            for col in range(c+direct,c+(n*direct)+direct,direct):
                res[r][col] = head.val
                head = head.next
                if not(head): return res
            c = col
            n -= 1
            for row in range(r+direct, r+(m*direct)+direct,direct):
                res[row][c] = head.val
                head = head.next
                if not(head): return res
            r = row
            direct = -1 if direct == 1 else 1
        return res