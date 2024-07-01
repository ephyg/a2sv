# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        degree=defaultdict(int)
        for i in range(len(recipes)):
            for sup in ingredients[i]:
                graph[sup].append(recipes[i])
            degree[recipes[i]]+=len(ingredients[i])

        queue=deque()
        for sup in supplies:
            queue.append(sup)
        for food in degree:
            if degree[food]==0:
                queue.append(food)
        res=set(recipes)
        ans=[]
        while queue:
            node = queue.popleft()
            if node in recipes:
                ans.append(node)
            for neigh in graph[node]:
                degree[neigh]-=1
                if degree[neigh]==0:
                    queue.append(neigh)
        return ans
                     

