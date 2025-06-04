# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLen(head):
            cnt = 0
            if not head:
                return 0
            while head:
                head = head.next
                cnt+=1
            return cnt

        headLen= getLen(head)
        
        if headLen ==1:
            return None

        if headLen == n:
            return head.next

        n = (headLen - n)
                
        # print(n)
        i=0
        curr = head
        while i<n:
            i+=1
            if i==n:
                curr.next =curr.next.next
            curr = curr.next
            
        
        return head