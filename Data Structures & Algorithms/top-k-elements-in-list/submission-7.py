class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1: First approach using sort
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # result = [num for num, cnt in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]

        # return result

        # 2: using bucket sort like approach

        count = {}
        freq = [[] for i in range(0, len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res






