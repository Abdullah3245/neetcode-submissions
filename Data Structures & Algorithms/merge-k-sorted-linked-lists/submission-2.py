# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        res = ListNode()
        curr = res
        heap = []
        for lst in lists:
            if lst:
                heapq.heappush(heap, NodeWrapper(lst))
        
        while heap:
            node_wrapper = heapq.heappop(heap)
            curr.next = node_wrapper.node
            curr = curr.next
            node_wrapper.node = node_wrapper.node.next

            if node_wrapper.node:
                heapq.heappush(heap, node_wrapper)

        return res.next
