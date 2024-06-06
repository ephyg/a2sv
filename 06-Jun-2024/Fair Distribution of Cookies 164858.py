# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        _min=float("inf")
        childs=[0]*k
        if len(cookies) == k:
            return max(cookies)
    

        def distribute(idx):
            nonlocal _min
            if idx>=len(cookies):
                _min=min(_min,max(childs))
                return
          
            for i in range(k):
                childs[i]+=cookies[idx]
                distribute(idx+1)
                childs[i]-=cookies[idx]

        distribute(0)
        return  _min