# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_=0
        arr=[]
        for i in range(len(words)):
            x={k for k in words[i]}
            arr.append((x,len(words[i])))
        for i in range(len(words)):
            for j in range(i,len(words)):
                z=arr[i][0].intersection(arr[j][0])
                if z==set():
                    max_=max(max_,arr[i][1]*arr[j][1])
        return max_