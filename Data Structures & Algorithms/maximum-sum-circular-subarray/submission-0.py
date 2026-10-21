class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        cur_max = best_max = nums[0]
        cur_min = best_min = nums[0]

        for i, x in enumerate(nums):
            total += x
            if i == 0:
                continue
            cur_max = max(x, cur_max + x)
            best_max = max(best_max, cur_max)
            cur_min = min(x, cur_min + x)
            best_min = min(best_min, cur_min)

        # all negative -> wrap case would give empty subarray
        if best_max < 0:
            return best_max
        return max(best_max, total - best_min)