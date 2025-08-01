"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue  = deque()
        if root:
            queue.append(root)
        
        while len(queue)>0:
            lsize = len(queue)
            prev = None
            for i in range(lsize):
                cur = queue.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
        return root





        