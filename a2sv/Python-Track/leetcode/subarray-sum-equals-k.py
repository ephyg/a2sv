class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        total=0
        ans=0
        for num in nums:
            total+=num
            diff=total-k
            if diff in dic:
                ans+=dic[diff]
            dic[total]=1+dic.get(total,0)
        return ans
            