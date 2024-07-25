# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pair = []
        for i in range(len(nums)):
            num = str(nums[i])
            temp = ""
            for j in range(len(num)):
                temp += str(mapping[int(num[j])])
            pair.append([int(temp),i,nums[i]])
        pair.sort()
        return [x for y,z,x in pair]