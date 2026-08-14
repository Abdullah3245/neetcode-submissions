"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            if node is None:
                return None
                
            clone_node = Node(node.val)
            visited[node] = clone_node

            for neighbor in node.neighbors:
                clone_neighbor = dfs(neighbor)
                clone_node.neighbors.append(clone_neighbor)
            return clone_node
        return dfs(node)

