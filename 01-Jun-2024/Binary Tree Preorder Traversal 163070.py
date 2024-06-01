# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        if not root:
            return []
        ls.extend([root.val])
        print(self.preorderTraversal(root.left))
        ls.extend(self.preorderTraversal(root.left))
        ls.extend(self.preorderTraversal(root.right))
        return ls
