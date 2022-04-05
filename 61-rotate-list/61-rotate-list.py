# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None or head.next==None or k==0:
            return head
        cur=head
        len=1
        while(cur.next!=None): 
            cur=cur.next
            len+=1
        print(len)
        cur.next=head
        k=k%len
        k=len-k
        print(k)
        while(k!=0):
            cur=cur.next
            k-=1
        print(k)
        head=cur.next
        cur.next=None
        return head
        
            