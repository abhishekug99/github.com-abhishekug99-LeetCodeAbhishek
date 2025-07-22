
# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #O(e+v)
        graphOldtoNew = {}

        def dfs(node):
            if node in graphOldtoNew:
                return graphOldtoNew[node] 
            clone = Node(node.val)
            graphOldtoNew[node] = clone
            for nbr in node.neighbors:
                clone.neighbors.append(dfs(nbr))
            return clone

        return dfs(node) if node else None
         

        


