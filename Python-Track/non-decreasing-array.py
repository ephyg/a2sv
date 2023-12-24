class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter=0
        ls=nums.copy()
        if(len(nums)<=1):
            return True
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                if(counter==1):
                    return False
                if(i>=2 and nums[i-2]>nums[i]):
                    nums[i]=nums[i-1]
                counter+=1
                print(nums)
        return True