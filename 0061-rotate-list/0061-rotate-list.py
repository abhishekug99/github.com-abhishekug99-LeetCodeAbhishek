# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        def getLen(head):
            cnt =0
            if not head:
                return None
            while head:
                head = head.next
                cnt+=1
            return cnt
        
        length = getLen(head)
        k = k % length
        if k == 0:
            return head
        cut = length - k

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        cur = head
        curD1 = dummy1
        curD2 = dummy2
        i=0
        while cur:
            if i<cut:
                curD1.next = cur
                curD1 = curD1.next
            else:
                curD2.next = cur
                curD2 = curD2.next
            i+=1
            cur = cur.next

        curD1.next = None
        curD2.next = dummy1.next

        return dummy2.next





        