class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        tot=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                tot+=nums[i]
        for i in range(len(queries)):
            before=nums[queries[i][1]]
            nums[queries[i][1]]+=queries[i][0]
            after=nums[queries[i][1]]
            if(before%2==0):
                if(after%2==0):
                    tot=tot-before+after
                else:
                    tot-=before
            else:
                if(after%2==0):
                    tot+=after
            ans.append(tot)
        return ans          
            