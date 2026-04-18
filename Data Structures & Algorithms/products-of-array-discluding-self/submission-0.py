class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n

        prefix[0] = nums[0]
        suffix[n-1] = nums[-1]
        # left to right multiplication - prefix
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]

        # right to left multiplication - suffix
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        # result
        for i in range(n):
            if i == 0:
                res[i] = suffix[i+1]
            elif i == n-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * suffix[i+1]
        
        return res
        