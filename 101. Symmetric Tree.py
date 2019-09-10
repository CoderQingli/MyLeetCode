def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return self.helper(root, root)


def helper(self, left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    return self.helper(left.left, right.right) and self.helper(left.right, right.left)