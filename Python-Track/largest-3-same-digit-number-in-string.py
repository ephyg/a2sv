class Solution:
    def largestGoodInteger(self,num: str) -> str:
        ans=[]
        for i in range(len(num)-2):
            temp=[num[i]]
            if("".join(temp*3))==num[i:i+3]:
                ans.append("".join(temp*3))
        if len(ans)>0:
        	ans.sort()
        	return ans[-1]
        else:
        	return ""