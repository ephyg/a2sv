class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def perm(ls,choice):
            if  len(ls) == len(nums):
                ans.append(ls[:])
                return

            for i in range(len(choice)):
                x=choice[:i]+choice[i+1:]
                ls.append(choice[i])
                perm(ls,x)
                ls.pop()
                
        perm([],nums[:])
        return ans