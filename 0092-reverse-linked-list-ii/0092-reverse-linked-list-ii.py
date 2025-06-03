# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newHead = ListNode(0,head)
        
        lPrev,curr = newHead, head
        for i in range(left-1):
            lPrev,curr = curr, curr.next
        
        prev = None
        for i in range(right -left +1):
            tmpNext = curr.next
            curr.next = prev
            prev,curr = curr, tmpNext
        
        #swap pointer
        lPrev.next.next = curr #curr node after right node
        lPrev.next = prev #prev node to right

        return newHead.next



              

        

        