class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_ = 0
        for i in range(len(trips)):
            max_=max(trips[i][2],max_)
        ls=[0]*(max_+1)

        for num, fro, to in trips:
            ls[fro]+=num
            ls[to]-=num

        for i in range(1,max_):
            ls[i]+=ls[i-1]
            if ls[i] > capacity:
                return False
        if ls[0] > capacity:
            return False
        return True
        
