class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=list(set(nums))
        ans=[]
        for i in range(len(x)):
            y=nums.count(x[i])
            if(len(nums)/3<y):
                ans.append(x[i])
        return ans