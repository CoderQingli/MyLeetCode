def minMoves(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_n = min(nums)
    for i in range(len(nums)):
        nums[i] -= min_n
    return sum(nums)