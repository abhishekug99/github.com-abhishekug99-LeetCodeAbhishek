"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        oldToNew= {}
        cur = head
        # 1st pass creating jus copy and keeping note of pointers in hash map
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next
        
        # print(oldToNew)
        # 2nd pass
        cur = head
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew.get(cur.next)
            copy.random = oldToNew.get(cur.random)
            cur = cur.next
        
        return oldToNew[head]

