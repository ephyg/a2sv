class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans=Counter(answers)
        tot=0
        for (key,value) in ans.items():
            mod=value % (key+1)
            if mod!=0:
                tot+=(key+1-mod)
            tot+=value
        return tot