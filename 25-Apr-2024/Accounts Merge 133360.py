# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails={}
        name={}
        rank=defaultdict(int)
        for value in accounts:
            for email in value[1:]:
                emails[email]=email
                name[email]=value[0]
        def find(x):
            if emails[x]==x:
                return x
            emails[x]=find(emails[x])
            return emails[x]
        def union(x,y):
            xx=find(emails[x])
            yy=find(emails[y])
            if xx!=yy :
                if rank[yy] < rank[xx]:
                    emails[yy] = xx
                elif rank[xx] < rank[yy]:
                    emails[xx] = yy
                else:
                    rank[xx]+=1
                    emails[yy]=xx
        
        for i in range(len(accounts)):
            for j in range(2,len(accounts[i])):
                union(accounts[i][j],accounts[i][j-1])
        result=defaultdict(list)
        for key,value in emails.items():
            result[find(value)].append(key)
        for key,value in result.items():
            result[key]=sorted(value)
        ans=[]
        for key in result:
            temp=[]
            temp.append(name[key])
            temp+=(result[key])
            ans.append(temp)
        return ans

