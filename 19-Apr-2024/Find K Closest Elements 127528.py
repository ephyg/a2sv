# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        left=0
        right=0
        bisect=bisect_left(arr,x)
        if bisect==len(arr):
            left=len(arr)-1
            right=len(arr)
        else:
            left=bisect-1
            right=bisect        
        ans=[]
        while k>0:
            if left>-1 and right<len(arr):
                res1=x-arr[left]
                res2=arr[right]-x
                if res1==res2:
                    ans.append(arr[left])
                    left-=1
                elif res1>res2:
                    ans.append(arr[right])
                    right+=1
                else:
                    ans.append(arr[left])
                    left-=1
            elif left>-1:
                ans.append(arr[left])
                left-=1
            else:
                ans.append(arr[right])
                right+=1
            k-=1
        return sorted(ans)


