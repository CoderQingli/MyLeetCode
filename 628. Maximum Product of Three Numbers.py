def maximumProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 3:
        return nums[0] * nums[1] * nums[2]
    if len(nums) == 4:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        nums.remove(max2)
        max3 = max(nums)
        min1 = min(nums)
        return max(min1 * max3 * max1, max1 * max2 * max3)
    max1 = max(nums)
    nums.remove(max1)
    max2 = max(nums)
    nums.remove(max2)
    max3 = max(nums)
    min1 = min(nums)
    nums.remove(min1)
    min2 = min(nums)
    return max(min1 * min2 * max1, max1 * max2 * max3)