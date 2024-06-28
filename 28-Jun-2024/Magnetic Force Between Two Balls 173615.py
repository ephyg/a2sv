# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def validate(mid):
            countBalls = 1
            prev = position[0]
            for i in range(1,len(position)):
                if (position[i] - prev >= mid):
                    countBalls += 1
                    prev = position[i]
            return countBalls >= m


        left,right,best = 1,max(position)-min(position),-1
        while right >= left:
            mid = left + (right - left) // 2
            if validate(mid):
                left = mid + 1
                best = mid
            else:
                right = mid - 1

        return best
