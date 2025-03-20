# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumLl = ListNode()
        curr = sumLl
        carry = 0
        curr1 = l1
        curr2 = l2
        while curr1 or curr2 or carry:
            if curr1:
                val1 = curr1.val
                curr1 = curr1.next
            else: val1 = 0

            if curr2:
                val2 = curr2.val
                curr2 = curr2.next
            else: val2 = 0
            
            currSum = val1 + val2 + carry
            carry  = currSum//10
            curr.next = ListNode(currSum%10)
            curr = curr.next
        
        return sumLl.next
        