# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthGrp(curr,k):
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr
        
        dummy = ListNode(0,head)
        grpPrev = dummy

        while True:
            kTh = getKthGrp(grpPrev,k)
            if not kTh:
                break
            grpNxt = kTh.next

            #reverse the group
            prev,curr = kTh.next, grpPrev.next
            while curr!=grpNxt:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = grpPrev.next
            grpPrev.next = kTh
            grpPrev = tmp

        return dummy.next




    #Stactic approach works for only two groups 
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     def lenght(head):
    #         if not head:
    #             return 0
    #         return 1 + lenght(head.next)

    #     def reverse(head):
    #         curr,prev = head, None
    #         while curr:
    #             temp = curr.next
    #             curr.next = prev
    #             prev = curr
    #             curr = temp
    #         return prev
    
    #     curr  = head
    #     p1 = ListNode()
    #     currp1 = p1
    #     p2 = ListNode()
    #     currp2 = p2
    #     i = 0
    #     while curr:
    #         if i<k:
    #             currp1.next = ListNode(curr.val)
    #             currp1 = currp1.next
                
    #         else:
    #             currp2.next = ListNode(curr.val)
    #             currp2 = currp2.next

            
    #         curr = curr.next
    #         i+=1
    #     # return p2.next
    #     p1Reversed = reverse(p1.next)
    #     p2Reversed = reverse(p2.next) if lenght(p2.next) >= k else p2.next

    #     # lenp2 = lenght(p2.next)

    #     currp1R = p1Reversed

    #     while currp1R and currp1R.next:
    #         currp1R = currp1R.next

    #     if currp1R:
    #         currp1R.next = p2Reversed
        
    #     return p1Reversed


        
        
        






        