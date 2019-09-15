def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums.count(0) > 1:
        return True
    return sum(nums) != sum(set(nums))