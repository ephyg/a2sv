class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot=skill[0]+skill[-1]
        left=0
        right=len(skill)-1
        res=0
        counter=0
        while right>left:
            add=skill[left]+skill[right]
            if add == tot:
                counter+=1
                res+=(skill[left]*skill[right])
                right-=1
                left+=1
            if add>tot:
                right-=1
            if tot>add:
                left+=1
        if counter==len(skill)//2:
            return res
        else:
            return -1
    