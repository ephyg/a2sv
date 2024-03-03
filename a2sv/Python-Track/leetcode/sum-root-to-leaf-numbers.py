# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def numbers(node,temp):
            nonlocal arr
            if not node:
                return 
            if node.left==None and node.right==None:
                temp.append(str(node.val))
                arr.append(int("".join(temp[:])))
                return 

            temp.append(str(node.val))
            numbers(node.left,temp[:])
            numbers(node.right,temp[:])
            
        numbers(root,[]) 
        print(arr)   
        return sum(arr)



        