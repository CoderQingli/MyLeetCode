def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    t = 1
    i = 0
    while t <= n:
        if nums[i] == 0:
            nums.append(nums.pop(i))
        else:
            i += 1
        t += 1