# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_a=headA
        node_b=headB
        dct=set()
        if not node_a or not node_b  :
            return
        if node_a==node_b:
            return node_a
        while node_a and node_a.next:
            dct.add(node_a)
            node_a=node_a.next
        while node_b and node_b.next:
            if node_b in dct:
                return node_b
            node_b=node_b.next
        if node_a==node_b:
            return node_a


