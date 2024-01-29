class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False
        i=0
        j=0
        while j<len(typed):
            if (i<len(name) and name[i]==typed[j]):
                i+=1
            else:
                if j==0 or typed[j]!=typed[j-1]:
                    return False
            j+=1
        return i==len(name)