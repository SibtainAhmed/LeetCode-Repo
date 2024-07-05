# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = prev.next
        res = [math.inf,-1]
        c_ps = []
        index = 1
        while curr.next:
            if prev.val > curr.val and curr.val < curr.next.val:
                c_ps.append(index)
            elif prev.val < curr.val and curr.val > curr.next.val:
                c_ps.append(index)
            curr, prev = curr.next, curr
            index += 1
        # print(c_ps)
        if len(c_ps) > 1:
            prev = c_ps[0]
            for i in range(1,len(c_ps)):
                curr = c_ps[i]
                res[0] = min(res[0], curr-prev)
                prev = curr
            res[1] = c_ps[-1] - c_ps[0]
            return res
        else:
            return [-1,-1]