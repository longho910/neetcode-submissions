class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        memo = {}

        def dfs(i, cur_total):
            if (i, cur_total) in memo:
                return memo[(i, cur_total)]
            if cur_total == total / 2:
                return True
            if i == len(nums) or cur_total > total / 2:
                return False
            memo[(i, cur_total)] = dfs(i + 1, cur_total + nums[i]) or dfs(i + 1, cur_total)
            return memo[(i, cur_total)]
        if dfs(0, 0):
            return True
        return False
