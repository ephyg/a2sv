class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s=[str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if s[i]+s[j]<s[j]+s[i]:
                    s[i],s[j]=s[j],s[i]
        ans="".join(s)
        return str(int(ans))
        
        
        