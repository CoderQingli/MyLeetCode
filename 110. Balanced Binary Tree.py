def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    left = self.maxdepth(root.left)
    right = self.maxdepth(root.right)
    return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


def maxdepth(self, root):
    if not root:
        return 0
    return max(self.maxdepth(root.left), self.maxdepth(root.right)) + 1