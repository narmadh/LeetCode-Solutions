# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        l=head
        r=head.next
        while r:
            if l.val==r.val:
                r=r.next
                l.next=r
            else:
                l=l.next
                r=r.next
        return head
            