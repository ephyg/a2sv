class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        dict={}
        for i,num in enumerate(nums):
            all_negative=(num<0 and nums[(i+num)%len(nums)]<0)
            all_positive=(num>0 and nums[(i+num)%len(nums)]>0)
            if i!=(i+num)%len(nums) and (all_negative or all_positive) :
                dict[i]=(i+num)%len(nums)
        print(dict)
        
        for v in dict:
            val=v
            flag=v
            i=0
            while dict[val] in dict and i<len(nums):
                val=dict[val]
                if val == flag:
                    return True
                i+=1
        return False