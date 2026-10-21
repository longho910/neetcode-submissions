# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a bucket list
        # [] [] [] .... [] based on frequency
        # for ex nums = [1,2,2,3,3,3]
        # [] [1] [2] [3] [] [] []
        # at most a number exists in n times

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0) # count = {1: 1, 2:2, 3:3}
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, cnt in count.items():
            freq[cnt].append(n) # freq = [[] [1] [2] [3] [] [] []]

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if len(res) == k:
                    break
                res.append(n)
                

        return res 

        