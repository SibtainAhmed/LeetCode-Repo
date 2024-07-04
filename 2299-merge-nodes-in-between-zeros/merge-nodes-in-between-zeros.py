# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        curSum = 0
        tempHead = head
        while curr:
            curSum += curr.val
            if curr.val == 0:
                curr.val = curSum
                curSum = 0
                tempHead.next = curr
                tempHead = curr
                if not head.val:
                    head = curr
            curr, prev = curr.next, curr
        return head