class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach 1: using sort function, T: O(nlogn), S: O(1)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # count = {1: 5, 2: 3, 3: 4}
        sort_arr = []
        for num in count:
            sort_arr.append((count[num], num))
        sort_arr.sort()
        # sort_arr = [[3, 2], [4, 3], [5, 1]]
        # k = 2
        # use pop
        res = []
        for i in range(k):
            res.append(sort_arr.pop()[1])
        return res







        # approach 2: using heap, T: O(nlogk), S: O(n + k)
        '''
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
        '''



