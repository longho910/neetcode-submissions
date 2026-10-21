class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1: First approach using sort
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        result = [num for num, cnt in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]

        return result