# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap=[]
        heapProcessingTime=[]
        for i in range(len(tasks)):
            heappush(heap,(tasks[i][0],tasks[i][1],i))
        ans=[]
        time=0
        for i in range(len(tasks)):
            enque,process,idx=0,0,0
            if not heapProcessingTime:
                enque,process,idx=heappop(heap)
                ans.append(idx)         
            else:
                process,idx,enque=heappop(heapProcessingTime)
                ans.append(idx)

            if enque>time:
                time+=(enque-time)
            time+=process  
            
            while heap and heap[0][0]<=time:
                heappush(heapProcessingTime,(heap[0][1],heap[0][2],heap[0][0]))
                heappop(heap)
        return ans

        

        