class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def helper(i, j):
            sum1, sum2 = 0, 0
            for i in range(i, j + 1):
                temp = max(nums[i] + sum1, sum2)
                sum1 = sum2
                sum2 = temp
            return sum2
        
        return max(nums[0], helper(0, n -2), helper(1, n -1))