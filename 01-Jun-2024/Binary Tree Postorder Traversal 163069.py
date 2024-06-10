# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        if root:
            if root.left:
                ls.extend(self.postorderTraversal(root.left))
            if root.right:
                ls.extend(self.postorderTraversal(root.right))
            ls.append(root.val)
        return ls
            