# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=max(candies)
        ans=[]
        for i in range(len(candies)):
            if((candies[i]+extraCandies)>=x):
                ans.append(True)
            else:
                ans.append(False)
        return ans