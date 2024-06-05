# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length=0
        countLength=head
        temp=head
        while countLength:
            length+=1
            countLength=countLength.next
        for i in range(length):
            while temp.next:
                if temp.val>temp.next.val:
                    temp.val,temp.next.val=temp.next.val,temp.val
                temp=temp.next
            temp=head
        return head

            