class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        count_with_even=0
        odd=0
        ans=0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                odd+=1
                count_with_even=0
            if k==odd:
                while left<len(nums) and nums[left]%2==0 :
                    count_with_even+=1
                    left+=1
                count_with_even+=1
                left+=1
                odd-=1 
            ans+=count_with_even
        return ans
