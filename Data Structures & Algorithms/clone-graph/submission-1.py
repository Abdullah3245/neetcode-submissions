"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        # we will perform BFS
        visited = set()
        visited.add(node)
        clone = Node(node.val)
        node_to_clone = {node: clone}
        queue = [(node, clone)]
        while len(queue) > 0:
            curr, curr_clone = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    # Case 1: New neighbor - create clone and add to queue
                    new_neighbor = Node(neighbor.val)
                    visited.add(neighbor)
                    node_to_clone[neighbor] = new_neighbor  # Store mapping
                    queue.append((neighbor, new_neighbor))
                    curr_clone.neighbors.append(new_neighbor)
                else:
                    # Case 2: Already visited - find existing clone and connect
                    existing_clone = node_to_clone[neighbor]
                    curr_clone.neighbors.append(existing_clone)
        return clone