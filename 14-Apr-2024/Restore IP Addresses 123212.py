# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]

        def backtrack(idx,curr):
            nonlocal ans
            if len(curr)==4 and idx==len(s):
                ans.append(".".join(curr))
                return
            if len(curr)==4 or idx==len(s):
                return
            for j in range(1,4):
                each=s[idx:idx+j]
                if len(each) > 1 and ( each[0] == '0' or int(each) > 255):
                    continue
                if len(curr)<4:
                    curr.append(each)
                    backtrack(idx+j,curr)
                    curr.pop()


        backtrack(0,[])
        return ans