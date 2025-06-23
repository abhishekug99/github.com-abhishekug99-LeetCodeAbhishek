# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        upper = ListNode(0)
        curLess = less
        curUpper = upper
        while head:
            if head.val<x:
                curLess.next = head
                curLess  = curLess.next
            else:
                curUpper.next = head
                curUpper = curUpper.next
            
            head = head.next
        curUpper.next = None
        curLess.next = upper.next
        return less.next
