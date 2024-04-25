# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        strs=sorted(list(set([i for i in s1+s2])))
        unionsets={i:i for i in strs}
        # print(unionsets)'
        rank=defaultdict(int)

        def find(x):
            if unionsets[x]==x:
                return x
            unionsets[x] = find(unionsets[x])
            return unionsets[x]

        def unions(x,y):
            xx=find(unionsets[x])
            yy=find(unionsets[y])
            if xx!=yy :
                if rank[yy] < rank[xx]:
                    unionsets[yy] = xx
                elif rank[xx] < rank[yy]:
                    unionsets[xx] = yy
                else:
                    rank[xx]+=1
                    unionsets[yy]=xx

        result=defaultdict(list)
        for i in range(len(s1)):
            unions(s1[i],s2[i])

        for keys,value in unionsets.items():
            result[find(keys)].append(keys)
        for keys,value in unionsets.items():
            result[keys].sort()
        # print(result)
        ans=""
        for let in baseStr:
            if let in result and result[let]:
                ans+=result[let][0]
            else:
                for key,value in result.items():
                    if let in value:
                        ans+=value[0]
                        break
                else:
                    ans+=let
                
                
        return ans
