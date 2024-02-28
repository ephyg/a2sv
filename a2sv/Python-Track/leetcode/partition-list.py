# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(None)
        dummy2 = ListNode(None)
        left = dummy1
        right = dummy2
                
        while head:
            if head.val < x:        
                left.next=head
                left=left.next
            else:
                right.next=head
                right=right.next
            head=head.next
        left.next=None
        right.next=None
        left.next=dummy2.next
        return dummy1.next
