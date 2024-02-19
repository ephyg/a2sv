class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=defaultdict(lambda :-1)
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                nums[stack[-1]]=num
                stack.pop()
            stack.append(num)
        return [nums[i] for i in nums1]