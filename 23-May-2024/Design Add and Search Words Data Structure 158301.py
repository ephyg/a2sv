# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[False for i in range(26)]
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for char in word:
            idx=ord(char)-97
            if not curr.children[idx]:
                curr.children[idx]=TrieNode()
            curr=curr.children[idx]
        curr.is_end=True  
              
    def search(self, word: str) -> bool:

        queue=deque([(self.root,0)])
        while queue:
            for i in range(len(queue)):
                trie,idx=queue.popleft()
                if idx>=len(word) and trie.is_end:
                    return True
                if idx<len(word):
                    if word[idx]==".":
                        for i in range(26):
                            if trie.children[i]:
                                queue.append((trie.children[i],idx+1))
                    elif trie.children[ord(word[idx])-97]:
                        queue.append((trie.children[ord(word[idx])-97],idx+1))

        return False
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)