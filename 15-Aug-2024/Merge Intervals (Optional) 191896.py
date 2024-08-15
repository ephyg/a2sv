# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack=[intervals[0]]
        for i in range(1,len(intervals)):
            if stack[-1][1]>=intervals[i][0]:
                if intervals[i][1]>=stack[-1][1]:
                    stack[-1][1]=intervals[i][1]
            else:
                stack.append(intervals[i])
        return stack