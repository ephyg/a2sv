# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        freq_s = defaultdict(int)
        for right in range(len(s)):
            freq_s[s[right]] += 1
            while left <= right and freq_s[s[right]] > 1:
                freq_s[s[left]] -= 1
                left += 1
            longest = max(longest,right - left +1)
        return longest
