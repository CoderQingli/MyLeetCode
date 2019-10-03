def longestUnivaluePath(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.res = 0
    if not root:
        return 0

    def helper(n):
        if not n:
            return 0
        left = helper(n.left)
        right = helper(n.right)
        l = r = 0
        if n.left and n.left.val == n.val:
            l = left + 1
        if n.right and n.right.val == n.val:
            r = right + 1
        self.res = max(self.res, l + r)
        return max(l, r)

    helper(root)
    return self.res