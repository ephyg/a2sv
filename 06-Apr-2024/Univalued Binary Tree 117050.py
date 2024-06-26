# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def bfs():
            deq=deque([root])
            org=root.val
            while deq:
                node=deq.popleft()
                if node.val!=org:
                    return False
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            return True
            
        return bfs()

