# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children  = [None]*26
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root=TrieNode()
        def insert(word):
            curr=root
            for char in word:
                idx = ord(char)-97
                if not curr.children[idx]:
                    curr.children[idx]=TrieNode()
                curr=curr.children[idx]
            curr.is_end=True

        def find(word):
            curr=root
            for i,char in enumerate(word):
                idx=ord(char)-97
                if curr.is_end:
                    return word[:i]
                if not curr.children[idx]:
                    return word
                curr=curr.children[idx]
            return word
        for word in dictionary:
            insert(word)
        
        ans=[]
        for word in sentence.split():
            ans.append(find(word))
        return " ".join(ans)

