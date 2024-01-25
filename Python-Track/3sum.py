class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result={}
        for  i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            target=0-nums[i]
            while right>left:
                _sum=nums[left]+nums[right]
                if _sum==target:
                    res=(nums[i],nums[left],nums[right])
                    if res in result:
                        result[res]+=1
                    else:
                        result[res]=1
                    right-=1
                    left+=1
                elif _sum>target:
                    right-=1
                else:
                    left+=1
        ans=[list(i) for i in list(result.keys())]
        return ans
