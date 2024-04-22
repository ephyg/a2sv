# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        level=0
        result=[[root.val]]
        while queue:
            bound=len(queue)
            temp=[]
            for i in range(bound):
                node=queue.popleft()
                if node.left:
                    temp.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
            if queue and level%2==0:
                result.append(temp[::-1])
            if queue and level%2:
                result.append(temp)
            level+=1
        return result
        
        
            
