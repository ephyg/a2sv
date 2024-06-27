# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        zero_index=m+n-1
        m=m-1
        n=n-1


        while n>=0:
            if(m>=0 and (nums1[m]>nums2[n])):
                nums1[zero_index]=nums1[m]
                m-=1
            else:
                nums1[zero_index]=nums2[n]
                n-=1
            zero_index-=1
        return nums1
