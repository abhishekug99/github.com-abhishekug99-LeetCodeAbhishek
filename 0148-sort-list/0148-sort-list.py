# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        vals.sort()
        sHead = ListNode(0)
        scur = sHead
        for val in vals:
            scur.next  = ListNode(val)
            scur = scur.next 

        return sHead.next