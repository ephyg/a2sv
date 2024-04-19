# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)

        def traverse(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                traverse(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                traverse(node.right)
        traverse(root)
        queue=deque([target])
        visited={target}
        while queue and k>0:
            bound=len(queue)
            for i in range(bound):
                node=queue.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
            k-=1

        ans=[]
        for node in queue:
            ans.append(node.val)
        
        return ans


