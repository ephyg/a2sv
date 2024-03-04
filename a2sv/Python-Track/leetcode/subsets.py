class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def sub(num,curr):
            if len(curr)<=len(nums):
                ans.append(curr[:])
            
            for i in range(len(num)):
                curr.append(num[i])
                sub(num[i+1:],curr)
                curr.pop()

        sub(nums[:],[])
        print(ans)
        return ans