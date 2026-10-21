class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur):
            # base case:
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            # explore choices
            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                dfs(cur)
                cur.pop()
        dfs([])
        return res