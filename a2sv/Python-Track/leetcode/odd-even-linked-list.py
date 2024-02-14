class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1=Node(None)
        dummy2=Node(None)
        temp1=dummy1
        temp2=dummy2
        h=temp1
        s=temp2
        count=0
        t=head
        while t:
            if count%2==0:
                temp1.next=t
                temp1=temp1.next
            else:
                temp2.next=t
                temp2=temp2.next
            t=t.next
            count+=1
        temp2.next=None
        if temp2:
            temp1.next=s.next
        return h.next
                