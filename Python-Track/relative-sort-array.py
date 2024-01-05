class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    ans.append(arr1[j])
        not_exist=[]
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                not_exist.append(arr1[i])
        not_exist.sort()
        return ans+not_exist

