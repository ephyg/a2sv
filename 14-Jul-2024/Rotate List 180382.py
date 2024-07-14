# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        temp=head
        slow=fast=head
        while temp:
            temp=temp.next
            length+=1
        if length==0:
            return 
        mod=k%length
        for i in range(mod):
            fast=fast.next
        while fast and fast.next:
            fast=fast.next
            slow=slow.next

        fast.next=head
        nxt=slow.next
        head=nxt
        slow.next=None
        return head


        