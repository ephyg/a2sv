# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.is_end=True
        self.children=[False]*26

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        words.sort(key=lambda x:-len(x))
        def insert(word):
            curr=root
            for char in word:
                idx = ord(char)-97
                if not curr.children[idx]:
                    curr.children[idx]=TrieNode()
                curr = curr.children[idx]
            curr.is_end = True
        def startsWith(prefix):
            curr=root
            for char in prefix:
                idx=ord(char)-ord("a")
                if not curr.children[idx]:
                    return False
                curr=curr.children[idx]
            return True
        ans=0
        for word in words:
            if not startsWith(word[::-1]):
                ans += len(word)+1
                insert(word[::-1])
        return ans

        # ans = 0
        # curr = root
        # for i in range(26):
        #     if curr.children[i]:
        #         ans+=1
        # words.sort(key=len,reverse=True)
        # ans=""
        # for i in range(len(words)):
        #     if not words[i]+"#" in ans:
        #         ans+=words[i]+"#"
        # return len(ans)


