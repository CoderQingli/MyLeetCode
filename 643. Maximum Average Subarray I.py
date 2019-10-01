def findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    if not nums or len(nums) < k:
        return
    s = sum(nums[0:k])
    res = s
    for i in range(1, len(nums) - k + 1):
        s = s - nums[i - 1] + nums[i + k - 1]
        res = max(res, s)
    return res * 1.0 / k