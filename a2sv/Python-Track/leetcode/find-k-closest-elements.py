class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx=bisect_left(arr,x)
        left=max(idx-k,0)
        right=min(len(arr)-1,idx+k-1)
        while right-left>k-1:
            if abs(x-arr[left])>abs(x-arr[right]):
                left+=1
            else:
                right-=1
        return arr[left:right+1]
        
            

