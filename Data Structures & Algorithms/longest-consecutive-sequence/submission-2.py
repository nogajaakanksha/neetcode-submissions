class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Brute force : O(n2)
        # res = 0
        # for num in nums:
        #     count = 0
        #     while num+1 in nums:
        #         count += 1
        #         num += 1
        #     res = max(1+count, res)
        # return res

        # Sorting
        res, i = 0, 0
        nums.sort()
        while i < len(nums):
            # initial check for duplicate
            # while i + 1 < len(nums) and nums[i+1] == nums[i]:
            #     i += 1

            count = 0
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                count += 1
                i += 1
                # check for duplicates
                while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                    i += 1
            res = max(res, count+1)
            i += 1
        return res


