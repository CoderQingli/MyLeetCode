def findLengthOfLCIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    max_cnt = 0
    tmp = 0
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            tmp = i
        max_cnt = max(max_cnt, i - tmp + 1)
    return max_cnt