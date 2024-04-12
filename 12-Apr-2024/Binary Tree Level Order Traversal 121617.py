# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        ans=[]
        if root:
            ans.append([root.val])
        visited=set()
        while queue:
            n=len(queue)
            curr=[]
            for i in range(n):
                node=queue.popleft()
                if node and node.left:
                    visited.add(node.left.val)
                    queue.append(node.left)
                    curr.append(node.left.val)
                if node and node.right :
                    queue.append(node.right)
                    visited.add(node.right.val)
                    curr.append(node.right.val)                
            if curr:
                ans.append(curr)
            
        return ans
                