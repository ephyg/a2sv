class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict={0:1}
        tot=0
        ans=0
        for i, num in enumerate(nums):
            tot+=num
            diff=tot-goal
            if diff in dict:
                ans+=dict[diff]
            dict[tot]=1+dict.get(tot,0)
        return ans

