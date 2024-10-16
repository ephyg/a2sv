# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem =  defaultdict(int)
        count = 0
        for num in arr:
            x = k - (num%k)
            if x in rem and rem[x]>0:
                count += 1
                rem[x]-=1
            else:
                if num%k ==0:
                    rem[k] += 1
                else:
                    rem[num%k] += 1
   
        return count >= len(arr)//2
                
                