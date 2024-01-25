class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        temp=float("inf")
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while right>left:
                res=(nums[left]+nums[right]+nums[i])
                _diff=abs(res-target)
                if target==res:
                    return target
                elif res>target:
                    if abs(temp-target)>_diff:
                        temp=res
                    right-=1
                else:
                    if abs(temp-target) >_diff:
                        temp=res
                        print(temp)
                    left+=1
        return temp