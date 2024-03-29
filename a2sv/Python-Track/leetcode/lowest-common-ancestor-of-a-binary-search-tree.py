# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if node.val > q.val and node.val>p.val:
                return lca(node.left)
            elif node.val < q.val and node.val< p.val:
                return lca(node.right)
            else:
                return node
        return lca(root)
