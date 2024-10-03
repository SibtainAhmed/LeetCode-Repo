# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not(lists): return None
        def merge(l,r):
            head = node = ListNode()
            while l and r:
                if l.val > r.val:
                    val = r.val
                    r = r.next
                else:
                    val = l.val
                    l = l.next
                node.next = ListNode(val)
                node = node.next
            if l:
                node.next = l
            else:
                node.next = r
            return head.next

        def recur(lst):
            ln = len(lst)
            if ln == 1:
                return lst[0]
            elif ln==2:
                return merge(lst[0],lst[1])
            else:
                l = recur(lst[:ln//2])
                r = recur(lst[(ln//2):])
                return merge(l,r)
        return recur(lists)