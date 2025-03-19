# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # i<=n/2-1means need to partition array and pair twin from both sides
        # Step 1: Find the middle of the linked list (slow-fast pointer)
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # return slow.val
        # To efficiently pair the first half with the second half, we:
        # Find the middle node (using the slow and fast pointer method).
        # Reverse the second half of the linked list.
        prev,curr = None, slow
        while curr:
            nxtTemp = curr.next
            curr.next = prev
            prev  = curr
            curr = nxtTemp
        

        # Compare and sum pairs from both halves simultaneously. 
        p1,p2 = head,prev
        twinSum = 0
        while p2:
            twinSum = max(twinSum, p1.val+p2.val)
            p1 = p1.next
            p2 = p2.next

        return twinSum


    
    
    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     def headSize(head):
    #         l = 0
    #         if not head:
    #             return 0
    #         else:
    #             return 1 + headSize(head.next)
    #     lenght = headSize(head)
    #     print(lenght)
        
    #     def getNodeById(head, idx):
    #         if not head:
    #             return 0
    #         curr = head
    #         currId = 0
    #         while head:
    #             if currId == idx:
    #                 return curr.val
    #             curr = curr.next
    #             currId+=1

    #     curr = head
    #     if lenght == 2:
    #         return curr.val+curr.next.val

    #     i=0
    #     sumTwin = 0
    #     while curr:
    #         neededId = lenght-1-i
    #         sumTwin = curr.val + getNodeById(head, neededId)
    #         curr = curr.next
    #         i+=1
    #     return sumTwin
        

        