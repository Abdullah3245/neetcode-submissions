# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = 1
        res = ListNode(0, head)
        node_before = res

        while start < left:
            node_before = head
            head = head.next
            start += 1

        start_head = head
        prev_node = head
        head = head.next

        while start < right:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
            start += 1


  
        node_before.next = prev_node

        start_head.next = head
        
        return res.next

