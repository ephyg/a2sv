class Solution:
    def reductionOperations(self, nums: List[int]) -> dict:
        counter = 0
        larger={}
        nums.sort()
        freq=Counter(nums)
        x=sorted(list(set(nums)))
        for i in range(1,len(x)):
            larger[x[i]]=i
        for i in larger:
            counter+=(larger[i]*freq[i])
            
        return counter
