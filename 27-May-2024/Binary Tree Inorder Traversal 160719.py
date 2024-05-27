# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inordertraverse(node):
            if not node:
                return
            inordertraverse(node.left)
            ans.append(node.val)
            inordertraverse(node.right)
        
        inordertraverse(root)
        return ans