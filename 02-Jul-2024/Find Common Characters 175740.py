# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        visited=set()
        for i in range(len(words[0])):
            min_=words[0].count(words[0][i])
            for j in range(len(words)):
                x=words[j].count(words[0][i])
                min_=min(x,min_)
            if words[0][i] not in visited:
                ans.extend([words[0][i]]*min_)
                visited.add(words[0][i])
        return ans

                
