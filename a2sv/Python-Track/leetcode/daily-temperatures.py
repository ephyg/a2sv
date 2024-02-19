class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count=defaultdict(lambda :0)
        stack=[]
        for i,num in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<num:
                count[(temperatures[stack[-1]],stack[-1])]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return [count[(temp,i)] for i,temp in enumerate(temperatures)]
