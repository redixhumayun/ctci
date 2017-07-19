class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dp = []
        maximum = nums[0]
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp.append(nums[i] + dp[i-1])
            else:
                dp.append(nums[i] + 0)
            maximum = max(dp[i], maximum)
        return maximum

        # for i in range(0, len(nums)): #this won't work for all negative numbers
        #     if res < 0:
        #         res = 0
        #     res += nums[i]
        #     maximum = max(maximum, res)
        # return maximum


solution = Solution()
result = solution.maxSubArray([-2,-11,-3,-4,-1,-2,-1,-5,-4])
print(result)
