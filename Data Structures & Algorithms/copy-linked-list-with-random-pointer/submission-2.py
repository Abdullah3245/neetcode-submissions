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
    # Edge cases
        if head is None:
            return head
        random_nodes = {}
        temp = head
        # First pass which will create a copy of the node
        while head is not None:
            new_node = Node(head.val)
            random_nodes[head] = new_node
            head = head.next
        head = temp
        Optional = Node(-1, random_nodes[head])
        # Connecting pointers
        while head is not None:
            curr_node = random_nodes[head]
            curr_node.next = random_nodes[head.next] if head.next else head.next
            curr_node.random = random_nodes[head.random] if head.random else head.random
            head = head.next

        return Optional.next   