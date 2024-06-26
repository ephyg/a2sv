# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            arr.append(node)
            traverse(node.right)
            
            
        traverse(root)

        # arr.sort()

        def construct(arr):
            if not arr:
                return None

            m=(len(arr))//2
            root = arr[m]
            root.left = construct(arr[:m])
            root.right = construct(arr[m+1:])

            return root

        return construct(arr)