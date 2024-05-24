# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        def insert(word):
            curr = root
            for char in word:
                idx = ord(char) - 97
                if not curr.children[idx]:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.is_end = True

        for word in words:
            insert(word)

        curr = root
        queue = deque()
        for i in range(26):
            if curr.children[i] and curr.children[i].is_end:
                queue.append([curr.children[i], [chr(i + 97)]])
        ans = ""
        while queue:
            trie, word = queue.popleft()
            count = 0
            # print(trie, word)
            for i in range(26):
                if trie.children[i] and trie.children[i].is_end:
                    word.append(chr(i + 97))
                    queue.append([trie.children[i], word[:]])
                    word.pop()
                    count += 1
            if count == 0:
                temp = "".join(word)
                if len(ans) < len(temp):
                    ans = temp

        return ans
