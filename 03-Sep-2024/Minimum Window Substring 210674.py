# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        freq_s = defaultdict(int)

        # def isExist(Freq_t,Freq_s):
        #     for char in Freq_t:
        #         if Freq_t[char]>Freq_s[char]:
        #             return False
        #     return True
        
        min_length = float("inf")
        answer = ""
        left = 0
        have, needed = 0, len(freq_t)

        for right in range(len(s)):
            char = s[right]
            freq_s[char] += 1
            if freq_t[char] == freq_s[char]:
                have += 1
            
            while have == needed:
                length = len(s[left:right+1])
                if min_length > length:
                    min_length = length
                    answer = s[left:right+1]

                freq_s[s[left]] -= 1
                if freq_t[s[left]] > freq_s[s[left]]:
                    have -= 1
                left += 1
        return answer

