class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans=Counter(answers)
        tot=0
        for (key,value) in ans.items():
            mod=value % (key+1)
            # print(mod,key,value)
            if mod!=0:
                tot+=(value+key+1-mod)
            else:
                tot+=value
        return tot