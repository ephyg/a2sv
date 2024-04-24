# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.smallest=[]
        self.largest=[]
        self.count=0

    def addNum(self, num: int) -> None:
        if self.count%2==0:
            if self.largest:
                if self.largest[0]<num:
                    x=heappop(self.largest)
                    heappush(self.smallest,-x)
                    heappush(self.largest,num)
                else:
                    heappush(self.smallest,-num)
            else:
                heappush(self.smallest,-num)
        else:
            if self.smallest:
                if -self.smallest[0]>num:
                    x=heappop(self.smallest)
                    heappush(self.largest,-x)
                    heappush(self.smallest,-num)
                else:
                    heappush(self.largest,num)
            else:
                heappush(self.largest,num)
        self.count+=1



    def findMedian(self) -> float:
        if self.count%2:
            return -self.smallest[0]
        else:
            return (-self.smallest[0]+self.largest[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()