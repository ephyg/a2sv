# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq=Counter(arr1)
        arr=set(arr2)
        remain=[]
        ans=[]
        for num in arr2:
            if num in arr1:
                ans.extend([num]*freq[num])
        for num in arr1:
            if num not in arr:
                remain.append(num)
        ans.extend(sorted(remain))
        return ans

