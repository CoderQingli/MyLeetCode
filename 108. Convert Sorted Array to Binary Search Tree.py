def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = self.sortedArrayToBST(nums[:mid])
    node.right = self.sortedArrayToBST(nums[mid + 1:])
    return node