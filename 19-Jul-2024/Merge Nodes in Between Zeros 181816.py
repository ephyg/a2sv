# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        nums = []
        while temp:
            nums.append(temp.val)
            temp = temp.next
        ans =[]
        left = 0
        while left < len(nums):
            temp=0
            while nums[left]:
                temp+=nums[left]
                left+=1
            if temp:
                ans.append(temp)
            left+=1
        # print(ans)
        dummy = ListNode()
        temp = dummy
        for num in ans:
            dummy.next= ListNode(num)
            dummy = dummy.next

        return temp.next

                