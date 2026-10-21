class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ex: nums = [3, 4, 5, 6]
        # {0: 3, 1: 4, 2: 5, 3: 6}
        check = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in check:
                return [check[complement], i]
            check[n] = i