class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        idx=0
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            idx=arr.index(max(arr[:i+1]))
            arr[:idx+1]=arr[:idx+1][::-1]
            arr[:i+1]=arr[:i+1][::-1]
            ans.append(idx+1)
            ans.append(i+1)
        return ans

