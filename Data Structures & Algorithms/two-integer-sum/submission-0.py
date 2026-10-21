class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap to make O(n) for time
        # space is O(n) too
        hashmap = {} # val -> index
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[nums[i]] = i
        