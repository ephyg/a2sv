# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if(num%3!=0):
            return []
        else:
            middle=num//3
            return [middle-1,middle,middle+1]
        
            