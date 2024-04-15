# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue=deque([root])
        ans=[root.val]
        while queue:
            bound=len(queue)
            curr=[]
            for i in range(bound):
                node=queue.popleft()
                if node.right:
                    curr.append(node.right.val)
                    queue.append(node.right)
                if node.left:
                    curr.append(node.left.val)
                    queue.append(node.left)
            if curr:
                ans.append(sum(curr)/len(curr))
        return ans