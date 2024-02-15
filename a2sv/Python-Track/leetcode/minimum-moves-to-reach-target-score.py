class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        var=target
        ans=0
        for i in range(maxDoubles):
            if var>1:
                if var%2==0:
                    ans+=1
                else:
                    ans+=2
                var//=2
        return ans+var-1