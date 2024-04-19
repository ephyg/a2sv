# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=defaultdict(int)
        for word in words:
            freq[word]+=1
        temp=[]
        for key,value in freq.items():
            heappush(temp,(-value,key))
        return [y for x,y in nsmallest(k,temp)]