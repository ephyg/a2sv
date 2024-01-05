class Solution:
    def smallestNumber(self, num: int) -> int:
        if(num<0):
            nums=[i for i in str(num)[1:]]
            nums.sort()
            
            nums=nums[::-1]
            ans=int("".join(nums))
            return ans-ans*2

        else:
            nums=[i for i in str(num)]
            nums.sort()
            if('0' in nums):
                for i in range(len(nums)):
                    if nums[i]!='0':
                        nums[0],nums[i]= nums[i],nums[0]
                        break
            ans="".join(nums)

            return int(ans)
        
