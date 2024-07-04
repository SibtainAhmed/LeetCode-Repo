# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextNode = head.next
        curr = nextNode
        while curr:
            curSum = 0
            while curr.val:
                curSum += curr.val
                curr = curr.next
            nextNode.val = curSum
            curr = curr.next
            nextNode.next = curr
            nextNode = curr

        return head.next