def __init__(self):
    self.res = float("inf")
    self.cur = float("-inf")


def getMinimumDifference(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return root
    self.getMinimumDifference(root.left)
    self.res = min(self.res, abs(root.val - self.cur))
    self.cur = root.val
    self.getMinimumDifference(root.right)
    return self.res