class Solution:
    def trap(self, height: List[int]) -> int:
        # approach 2: 2 pointers
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res






        # approach 1: prefix, postfix
        # to store maxL, maxR
        '''
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        res = [0] * n
        # curr value
        maxL = 0
        maxR = 0
        maxLeft[0] = maxRight[n-1] = 0
        for i in range(1, n):
            maxL = max(maxL, height[i-1])
            maxLeft[i] = maxL
        for i in range(n-2, -1, -1):
            maxR = max(maxR, height[i+1])
            maxRight[i] = maxR
        
        sum = 0
        for i in range(n):
            amount = min(maxLeft[i], maxRight[i]) - height[i]
            if amount > 0:
                res[i] = amount
                sum += amount
        return sum
        '''





