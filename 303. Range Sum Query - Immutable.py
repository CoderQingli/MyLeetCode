def __init__(self, nums):
    """
    :type nums: List[int]
    """
    self.tmp = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        self.tmp[i + 1] = self.tmp[i] + nums[i]


def sumRange(self, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """
    return self.tmp[j + 1] - self.tmp[i]