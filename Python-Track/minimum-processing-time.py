class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        _max=0
        for i in range(1,len(processorTime)+1):
            exec_ = tasks[(i*4)-1]+processorTime[i-1]
            _max = max(_max,exec_)
        return _max