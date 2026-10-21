class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Approach 1: prefix, postfix
        n = len(nums)
        res = [1] * n
        prefix = [1] * (n + 1)
        postfix = [1] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        print(prefix)
        
        for i in range(n - 1, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]
        
        print(postfix)
        for i in range(n):
            res[i] = prefix[i] * postfix[i+1]
        return res
        

        # Approach 2: prefix, postfix optimized
        '''
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        '''
        