# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[False for i in range(2)]
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root=TrieNode()
        def insert(binary):
            curr=root
            for char in binary:
                if not curr.children[int(char)]:
                    # print(char)
                    curr.children[int(char)]=TrieNode()
                curr=curr.children[int(char)]
            curr.is_end=True

        x=len(bin(max(nums))[2:])
        for num in nums:
            y=bin(num)[2:]
            binary="0"*(x-len(y))+y
            insert(binary)
        max_=0
        for num in nums:
            curr=root
            y=bin(num)[2:]
            binary="0"*(x-len(y))+y
            tot=0
            for i in range(len(y)):
                bits=int(binary[i])
                if bits==1:
                    if curr.children[0]:
                        tot+=2**(x-i-1)
                        curr=curr.children[0]
                    else:
                        curr=curr.children[1]
                else:
                    if curr.children[1]:
                        tot+=2**(x-i-1)
                        curr=curr.children[1]
                    else:
                        curr=curr.children[0]
            max_=max(tot,max_)
        return max_
                


        