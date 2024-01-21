class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target=Counter(s1)
        wind=Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1)+1):
            if target==wind:
                return True
            if (i+len(s1))<=len(s2)-1:
                if s2[i+len(s1)] in wind:
                    wind[s2[i+len(s1)]]+=1
                else:
                    wind[s2[i+len(s1)]]=1
            wind[s2[i]]-=1
            if wind[s2[i]]==0:
                wind.pop(s2[i])

        return False
