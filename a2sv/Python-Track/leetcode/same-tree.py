# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(p,q):
            if p and q:
                if q.val==p.val:
                    return same(p.left,q.left) and same(p.right,q.right)
                return False
            if not q and not p:
                return True
        return same(p,q)
