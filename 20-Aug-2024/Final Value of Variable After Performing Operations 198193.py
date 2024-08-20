# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operation = {"X++":1,"++X":1,"--X":-1,"X--":-1}
        ans=0
        for key in operations:
            ans+=operation[key]
        return ans