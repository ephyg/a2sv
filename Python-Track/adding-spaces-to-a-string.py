class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        x=s[:spaces[0]]
        for i in range(1,len(spaces)):
            x+=" "
            x+=s[spaces[i-1]:spaces[i]]
        x+=" "
        x+=s[spaces[-1]:]
        return x