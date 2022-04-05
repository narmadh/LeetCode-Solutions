"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return
        cur=head
        while cur!=None:
            new = Node(cur.val)
            new.next=cur.next
            cur.next=new
            cur=cur.next.next
        cur=head
        #print(cur.next.random,cur.next.val)
        while cur!=None:
            if cur.random==None:
                pass
            else:
                cur.next.random=cur.random.next
            cur=cur.next.next
        cur=head
        dup=head.next
        while cur.next!=None:
            tmp=cur.next
            cur.next=cur.next.next
            cur=tmp
        return dup
				


