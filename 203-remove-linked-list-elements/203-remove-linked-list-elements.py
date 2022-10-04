# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return head
        dummy=ListNode()
        dummy.next=head
        temp=head
        prev=dummy
        while(temp):
            #print(temp.val,prev.val)
            if temp.val==val:
                prev.next=temp.next
            else:
                prev=temp
            temp=temp.next
        return dummy.next