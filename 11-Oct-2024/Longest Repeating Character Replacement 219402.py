# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq_s = defaultdict(int)
        left = 0
        longest = 0

        for right in range(len(s)):
            freq_s[s[right]] += 1
            while left <= right and (right -left + 1) - max(freq_s.values()) > k:
                freq_s[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
