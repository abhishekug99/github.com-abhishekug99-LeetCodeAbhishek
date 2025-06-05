# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0,None)
        mapNode = {}
        cur = head
        while cur:
            if cur.val not in mapNode:
               mapNode[cur.val] = 1
            else:
                mapNode[cur.val] +=1
            cur = cur.next
        print(mapNode)
        cur = head
        dummyCur = dummy #alway modify with the copy of cur of head as it will be precise 
        while cur:
            if  mapNode[cur.val]>1:
                cur = cur.next
            elif mapNode[cur.val]==1:
                dummyCur.next = cur
                dummyCur = dummyCur.next
                cur = cur.next
        
        dummyCur.next = None # imp as it stops the LL on spot
        return dummy.next

        
        # cur = head
        # prev = None
        # while cur:
        #     prev = cur
        #     cur = cur.next
        #     if prev.next.val == cur.val and cur.next:
        #         prev.next = cur.next

            
        # return head
        