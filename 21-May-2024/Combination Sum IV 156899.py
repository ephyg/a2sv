# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo={}
        def dp(num):
            if num==0:
                return 1
            if num<0:
                return 0
            if num not in memo:
                t=0
                for i in nums:
                    t+=dp(num-i)
                memo[num]=t
            return memo[num]
        
        return dp(target)

        # dp=[0]*(target+1)
        # dp[0]=1

        # # count=0
        # # for num in nums:
        # #     if target%num==0:
        # #         count+=1
        # temp=[1]*(target+1)
        # for num in nums:
        #     for i in range(target-num+1):
        #         dp[num+i]+=dp[i]
        #         # dp[num+i]*=dp[i]
        #         temp[num+i]*=dp[i]
        # return dp[target]
