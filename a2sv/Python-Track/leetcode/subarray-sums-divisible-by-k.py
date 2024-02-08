class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict={0:1}
        tot=0
        ans=0
        for num in nums:
            tot+=num
            mod=tot%k
            if mod in dict:
                ans+=dict[mod]
            dict[mod]=1+dict.get(mod,0)
        return ans

