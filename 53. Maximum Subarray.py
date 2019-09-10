def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return None
    res = nums[0]
    tmp = nums[0]
    for i in range(1, len(nums)):
        tmp = max(tmp + nums[i], nums[i])
        res = max(res, tmp)
    return res

    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return None
    #     res = max(nums)
    #     for i in range(len(nums)):
    #         tmp = nums[i]
    #         j = i + 1
    #         while tmp >= 0 and j < len(nums):
    #             tmp += nums[j]
    #             if tmp >= res:
    #                 res = tmp
    #             j += 1
    #     return res