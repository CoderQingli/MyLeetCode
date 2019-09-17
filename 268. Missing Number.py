def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s1 = sum(nums)
    s2 = (1 + len(nums)) * len(nums) / 2
    return s2 - s1