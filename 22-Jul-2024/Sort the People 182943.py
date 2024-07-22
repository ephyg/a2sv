# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped=list(zip(heights,names))
        zipped.sort(reverse=True)
        return [name for height,name in zipped]
        




            