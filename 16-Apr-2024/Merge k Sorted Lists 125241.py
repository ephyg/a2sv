# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]

        for head in lists:
            while head:
                heappush(heap, head.val)
                head=head.next
        
        dummy=ListNode(None)
        temp=dummy
        for i in range(len(heap)):
            temp.next=ListNode(heappop(heap))
            temp=temp.next
        return dummy.next