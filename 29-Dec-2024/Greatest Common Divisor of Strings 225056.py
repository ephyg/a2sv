# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        first = 0
        second = 0
        ans = ""
        temp = ""
        while first <  len(str1) and second < len(str2):
            if str1[first] == str2[second]:
                if str1.count(ans+str1[first])*(len(ans)+1)==len(str1):
                    if str2.count(ans+str2[second])*(len(ans)+1)==len(str2):
                        temp = ans+str2[second]
            ans += str1[first]
            first += 1
            second += 1
        return temp