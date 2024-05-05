# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits=[0]*32
        neg=0
        for i in range(len(nums)):
            j=0
            temp=nums[i]
            if temp<0:
                temp=abs(nums[i])
                neg+=1
            while temp:
                if temp&1:
                    bits[j]+=1
                temp>>=1
                j+=1
        ans=0
        for i in range(32):
            if bits[i]%3:
                ans+=pow(2,i)
        return ans if neg%3==0 else -ans
