class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict={}
        for i in range(len(s)):
            dict[s[i]]=i
        ans=[]
        start=end=0
        for i in range(len(s)):
            end=max(end,dict[s[i]])
            if i==end:
                ans.append(end-start+1)
                start=(i+1)
        return ans
