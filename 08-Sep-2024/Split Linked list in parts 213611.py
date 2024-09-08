# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head 
        while temp:
            length += 1
            temp = temp.next
        ans = []
        equal = length // k
        iteration = [equal]*k
        remain = length % k
        for i in range(remain):
            iteration[i] += 1
        
        for i in range(k):
            dummy = ListNode()
            temp = dummy
            for j in range(iteration[i]):
                dummy.next = head
                head = head.next
                dummy=dummy.next
            dummy.next = None
            ans.append(temp.next)
        return ans
