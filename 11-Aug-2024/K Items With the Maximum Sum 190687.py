# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        for i in range(k):
            if numOnes!=0:
                ans+=1
                numOnes-=1
            elif numZeros!=0:
                ans+=0
                numZeros-=1
            else:
                ans-=1
                numNegOnes-=1
        return ans