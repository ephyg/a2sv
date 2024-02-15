class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        for i in range(maxDoubles):
            if target>1:
                if target%2==0:
                    ans+=1
                else:
                    ans+=2
                target//=2
        return ans+target-1