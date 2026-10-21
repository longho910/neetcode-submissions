class Solution:
    def trap(self, height: List[int]) -> int:
        # approach 1: use additional array
        # to store maxL, maxR
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





