# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None: return False
        fast=head
        slow=head
        while(fast.next is not None and fast.next.next is not None):
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                return True
        return False
            
        