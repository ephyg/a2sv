class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(left,right):
            if left==right:
                return nums[right]
            leftNum=nums[left]-rec(left+1,right)
            rightNum=nums[right]-rec(left,right-1)
            max_=max(leftNum,rightNum)
            return max_

            
        if rec(0,len(nums)-1)>=0:
            return True
        return False
        

