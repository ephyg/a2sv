# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def range(node):
            nonlocal ans
            if not node:
                return 
            
            if low <= node.val and high >= node.val:
                ans+=node.val
            range(node.left)
            range(node.right)
        range(root)
        return ans