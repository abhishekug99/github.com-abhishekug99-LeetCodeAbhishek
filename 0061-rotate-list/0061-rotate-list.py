# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        def getlenLL(head):
            if not head:
                return 0
            return 1 + getlenLL(head.next)
        
        length = getlenLL(head)
        if k == 0:
            return head
        k = k % length
        
        cut = length - k
        
        d1 = ListNode(0)
        d2 = ListNode(0)

        curr = head
        c1 = d1
        c2 = d2
        i=0

        while curr:
            if i<cut:
                c1.next = curr
                c1 = c1.next
            else:
                c2.next = curr
                c2 = c2.next
            
            i+=1
            curr=curr.next
        c1.next = None
        c2.next  = d1.next

        return d2.next





