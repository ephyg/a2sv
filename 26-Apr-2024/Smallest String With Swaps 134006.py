# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        letter={(let,i):(let,i) for i,let in enumerate(s)}
        rank=defaultdict(int)
        def find(x):
            if letter[x]==x:
                return x
            letter[x] = find(letter[x])
            return letter[x]

        def unions(x,y):
            xx=find(letter[x])
            yy=find(letter[y])
            if xx!=yy :
                if rank[yy] < rank[xx]:
                    letter[yy] = xx
                elif rank[xx] < rank[yy]:
                    letter[xx] = yy
                else:
                    rank[xx]+=1
                    letter[yy]=xx
        for x,y in pairs:
            unions((s[x],x),(s[y],y))
        arranged=defaultdict(list)
        for key,value in letter.items():
            arranged[find(value)].append(key)
        for key,value in letter.items():
            arranged[key].sort(reverse=True)
        ans=""
        for i,ss in enumerate(s):
            x=find((ss,i))
            if arranged[x]:
                res=arranged[x].pop()
                ans+=res[0]
        return ans
