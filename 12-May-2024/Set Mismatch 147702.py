# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        double=0
        nonexist=0
        for i in range(1,len(nums)+1):
            if freq[i]==2:
                double=i
            if freq[i]==0:
                nonexist=i
        return [double,nonexist]