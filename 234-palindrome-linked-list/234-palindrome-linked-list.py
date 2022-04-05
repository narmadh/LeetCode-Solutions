# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList (self,head:ListNode):
            pre=None
            Next=None
            while(head!=None):
                Next=head.next
                head.next=pre
                pre=head
                head=Next
            return pre
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None: return True
        slow=head
        fast=head
        while(fast.next is not None and fast.next.next is not None):
            slow=slow.next
            fast=fast.next.next
        slow.next=self.reverseList(slow.next)
        slow=slow.next
        while(slow!= None):
            if head.val!=slow.val:
                return False
            head=head.next
            slow=slow.next
        return True
    
        
        