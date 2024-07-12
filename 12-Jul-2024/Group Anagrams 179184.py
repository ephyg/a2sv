# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in range(len(strs)):
            x=[i for i in strs[i]]
            x.sort()
            x="".join(x)
            if x in dict:
                dict[x].append(strs[i])
            else:
                dict[x]=[strs[i]]
        return list(dict.values())
