# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def lenght(head: Optional[ListNode]):
            if not head:
                return 0
            else:
                return 1+lenght(head.next)
        headLen = lenght(head)
        
        if headLen == 1:
            return 
        
        midIndex = headLen//2 
        curr = head
        i = 0
        while curr is not None:
            if i == midIndex:
                break
            prev = curr
            curr = curr.next
            i+=1
        if curr == None:
            return
        prev.next  = curr.next
        curr = None
        return head

        # print(headList)