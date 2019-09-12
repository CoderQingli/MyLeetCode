def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = 0
    for num in nums:
        if cnt == 0:
            m = num
        if num == m:
            cnt += 1
        else:
            cnt -= 1
    return m

# def majorityElement(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     nums.sort()
#     return nums[len(nums) // 2]