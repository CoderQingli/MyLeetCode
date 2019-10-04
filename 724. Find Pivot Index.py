def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = sum(nums)
    tmp = 0
    for i in range(len(nums)):
        if tmp == s - tmp - nums[i]:
            return i
        tmp += nums[i]
    return -1