# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mainHead = ListNode(0, head)
        # node = head
        while head.next:
            if head.val < head.next.val:
                tempHead = mainHead
                while tempHead.next.val >= head.next.val:
                    tempHead = tempHead.next
                tempHead.next = head.next
            head = head.next
        return mainHead.next