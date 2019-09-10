class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            sub = target - nums[i]
            if sub in nums and nums.index(sub) != i:
                return [i, nums.index(sub)]
        return None