# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([root])
        ans=0
        while queue:
            bound=len(queue)
            temp=ans
            for i in range(bound):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                    ans=max(temp+1,ans)
                if node.right:
                    queue.append(node.right)
                    ans=max(temp+1,ans)
        return ans+1


                