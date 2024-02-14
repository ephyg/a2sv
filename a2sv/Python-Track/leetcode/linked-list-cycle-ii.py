# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return 

        left = right = slow=fast=head
        findIntersec = False
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                right=fast
                findIntersec = True
                break
        if not findIntersec:
            return
        while left is not right:
            left = left.next
            right = right.next
        
        return right
        