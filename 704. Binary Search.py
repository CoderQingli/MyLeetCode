def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return -1
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1