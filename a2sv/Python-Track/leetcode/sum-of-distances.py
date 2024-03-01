class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr = defaultdict(list)
        for i, num in enumerate(nums):
            arr[num].append(i)
        prefix = defaultdict(int)
        for key, val in arr.items():
            tot = sum(val)
            pre = 0
            for i, num in enumerate(val):
                pre += num
                left = (i + 1) * num - pre
                right = (tot - pre) - (len(val) - 1 - i) * num
                prefix[num] = left + right
        return [prefix[i] for i in range(len(nums))]
