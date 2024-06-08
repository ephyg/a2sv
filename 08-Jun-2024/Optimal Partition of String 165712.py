# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        stack=set()
        count=1
        for char in s:
            if char not in stack:
                stack.add(char)
            else:
                stack={char}
                count+=1
        return count
