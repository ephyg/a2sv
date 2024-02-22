class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numbers=defaultdict(lambda:-1)
        n=len(nums)
        ls=nums+nums
        stack=[]
        for i,num in enumerate(ls):
            if not stack:
                stack.append((i%n,num))
            else:
                while stack and stack[-1][1]<num:
                    numbers[(stack[-1][0],stack[-1][1])]=num
                    stack.pop()
                stack.append((i%n,num))
                
        return [numbers[(i,nums[i])] for i in range(len(nums))]

