class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        basket=defaultdict(int)
        ans=0
        for right in range(len(fruits)):
            basket[fruits[right]]+=1
            while len(basket)>2 and left<len(fruits) :
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    basket.pop(fruits[left])
                left+=1
            ans=max(sum(basket.values()),ans)
        return ans