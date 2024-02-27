class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search (node):
            if node:
                if node.val > val:
                    return search(node.left)
                if node.val < val:
                    return search(node.right)
                return node

        return search(root)
            