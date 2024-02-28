# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(None)
        dummy.next=head
        temp=dummy
        prev=dummy
        for i in range(left):
            temp=temp.next
            if i<left-1:
                prev=prev.next
        

        nxt=None
        curr=temp
        i=left
        while curr and i<=right:
            var=curr.next
            curr.next=nxt
            nxt=curr
            curr=var
            i+=1

        prev.next=nxt
        temp.next=curr
        return dummy.next
