class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles=[i for i in range(len(s)) if s[i]=="|"]
        ans=[]
        for left,right in queries:
            x=bisect_left(candles,left)
            y=bisect_right(candles,right)
            if x==y:
                ans.append(0)
                continue
            ans.append((candles[y-1]-candles[x])-(y-x-1))
        return ans
