# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A=0
        B=0
        hA=headA
        hB=headB
        while hA:
            A+=1
            hA=hA.next
        while hB:
            B+=1
            hB=hB.next
        if A>B:
            for i in range(A-B):
                headA=headA.next
        else:
            for i in range(B-A):
                headB=headB.next
        
        while headA:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None