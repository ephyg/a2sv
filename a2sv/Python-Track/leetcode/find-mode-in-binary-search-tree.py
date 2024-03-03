# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count=defaultdict(int)
        def mode(node):
            nonlocal count
            if not node:
                return 
            count[node.val]+=1
            mode(node.left)
            mode(node.right)
        mode(root)
        max_=max(list(count.values()))
        return [i for i in count if count[i]==max_]