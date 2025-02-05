"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {}

        def helper(node):
            if node in visited:
                return visited[node]

            new_node = Node(node.val)
            visited[node] = new_node
            #recursively create all neighbors
            for neigh in node.neighbors:
                new_node.neighbors.append(helper(neigh))

            return new_node

        return helper(node)

        