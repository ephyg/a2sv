# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic=Counter(nums)
        ans=0
        ls=dic.keys()
        for i in ls:
            if(dic[i]>1):
                a=factorial(dic[i])
                b=factorial(dic[i]-2)
                c=a/(b*2)
                ans+=c
        return int(ans)