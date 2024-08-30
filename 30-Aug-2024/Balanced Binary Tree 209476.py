# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(tree):
            height = defaultdict(int)
            stack =[(tree,False)]
            while stack:
                node, visited = stack.pop()
                if visited:
                    left_height = height[node.left]
                    right_height = height[node.right]
                    if abs(left_height - right_height) > 1:
                        return False
                    height[node] = 1 + max(left_height, right_height)
                else:
                    stack.append((node,True))
                    if node.right:
                        stack.append((node.right,False))
                    if node.left:
                        stack.append((node.left,False))
            return True
        return dfs(root)

        

        


        

            