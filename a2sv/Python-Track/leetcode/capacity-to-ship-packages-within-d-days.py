class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(limit):
            count=1
            capacity=0
            for i,num in enumerate(weights):
                capacity+=num
                if capacity>limit:
                    count+=1
                    capacity=num
            return count
        left,right,best=max(weights),sum(weights),float("inf")
        while left<=right:
            mid=left+(right-left)//2
            if validate(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
        return best

