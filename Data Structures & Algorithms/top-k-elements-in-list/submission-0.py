class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach 2: using heap
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))
            # maintain length of heap = k
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res



