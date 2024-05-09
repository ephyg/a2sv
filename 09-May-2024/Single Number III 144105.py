# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        XOR=0
        for num in nums:
            XOR^=num
        firstOneBit=0
        temp=XOR
        i=0
        while temp:
            if temp&1:
                firstOneBit=2**i
                break
            temp>>=1
            i+=1
        num1=0
        for num in nums:
            if num&firstOneBit:
                num1^=num
        return [num1,XOR^num1]