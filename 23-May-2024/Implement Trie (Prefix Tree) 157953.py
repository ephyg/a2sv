# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr=self.root
        for char in word:
            idx=ord(char)-ord("a")
            if not curr.children[idx]:
                curr.children[idx]=TrieNode()
            curr=curr.children[idx]
        curr.is_end=True
    def search(self, word: str) -> bool:
        curr=self.root
        for char in word:
            idx=ord(char)-ord("a")
            if not curr.children[idx]:
                return False
            curr=curr.children[idx]
        if curr.is_end:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for char in prefix:
            idx=ord(char)-ord("a")
            if not curr.children[idx]:
                return False
            curr=curr.children[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)