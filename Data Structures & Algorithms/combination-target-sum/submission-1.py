class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            # base case 
            if total == target:
                res.append(cur[:])
                return
            if total > target or i == len(nums):
                return

            # include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # not inclue nums[i]
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res