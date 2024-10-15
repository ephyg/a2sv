# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        ans = 0
        flag = False
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                count += 1
                flag = True
            else:
                if flag:
                    ans += count
        return ans

        