# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        def helper(mid):
            prev = start[0]
            for i in range(1,len(start)):
                if prev+mid <= start[i]:
                    prev = start[i]
                elif prev+mid <= start[i]+d:
                    prev = prev+mid
                else:
                    return False
            return True

        left,right,best = 0,start[-1]+d,0
        while right >= left:
            mid = left + (right - left) // 2
            if helper(mid):
                left = mid + 1
                best = mid
            else:
                right = mid - 1
        return best