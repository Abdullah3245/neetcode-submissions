# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False

        if head.next.next is None:
            return False

        fast = head.next.next
        slow = head
        while fast != slow and (fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next

        print(fast.val)
        if fast.next.next is None:
            return False
        return True
        