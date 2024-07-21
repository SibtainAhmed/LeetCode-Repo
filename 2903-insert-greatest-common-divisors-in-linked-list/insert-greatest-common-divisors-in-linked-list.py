# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        while curr:
            node = ListNode(math.gcd(prev.val,curr.val),curr)
            prev.next = node
            prev = curr
            curr = curr.next
        return head