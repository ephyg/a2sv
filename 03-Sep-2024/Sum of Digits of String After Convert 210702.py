# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums=""
        for i in range(len(s)):
            nums+=str(ord(s[i].lower())-96)
        for i in range(k):
            temp=0
            for num in nums:
                temp+=int(num)
            nums=str(temp)
        return int(nums)





